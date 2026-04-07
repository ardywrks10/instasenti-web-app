from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import StreamingResponse
from app.services.scraper import scrape_comment
from app.services.inference import predict_sentiment_batch
from app.services.analyzer import analyze_results
from typing import Optional, List
from pydantic import BaseModel

import io
import pandas as pd

router = APIRouter()

@router.post("/analyze/instagram")
async def analyze_instagram(
        username: str = Form(...),
        rangeMode: str = Form(...),
        customRange: Optional[str] = Form("")):
    try:
        comments, times, total_post, selected_post = scrape_comment(
            target_username = username, 
            range_mode      = rangeMode,
            custom_range    = customRange
        )

        if not comments:
            raise HTTPException(status_code=400, detail="Not Found any Comment")
        
        results = predict_sentiment_batch(comments)

        all_data = []
        for text, label, time in zip(comments, results, times):
            all_data.append({
                "text" : text,
                "label": label,
                "time" : time 
            })
            
        summary = analyze_results(results)
        top_5   = all_data[:5]

        return {
            "status": "success",
            "total_comments": len(comments),
            "total_post": total_post,
            "selected_post": selected_post,
            "summary": summary,
            "full_data": all_data,
            "top_5_comments": top_5
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))
    

class ExportRequest(BaseModel):
    data: List[dict]

@router.post("/analyze/instagram/export")
async def export_instagram_excel(payload: ExportRequest):
    try:
        df = pd.DataFrame(payload.data)
        
        if df.empty:
            raise HTTPException(status_code=400, detail="Data kosong")

        column_mapping = {
            "text": "Comment",
            "label": "Sentiment",
            "time": "Timestamp"
        }
        
        df = df.rename(columns=column_mapping)

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Results')
        
        output.seek(0)
        return StreamingResponse(
            output,
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': 'attachment; filename="InstaSenti_Export.xlsx"'}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal Export: {str(e)}")