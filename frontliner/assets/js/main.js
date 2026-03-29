const { createApp } = Vue;

createApp({
    data() {
        return {
            isMobileMenuOpen: false,
            menuItems: [
                { id: 1, name: 'Home', link: '#home' },
                { id: 2, name: 'Resources', link: '#resources' },
                { id: 3, name: 'About', link: '#about' },
            ],
            activeTab: 'tech',
            techItems: [
                {
                    id: 1,
                    name: 'Python',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 9H5a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h3"></path><path d="M12 15h7a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3"></path><path d="M8 9V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v5a4 4 0 0 1-4 4H4"></path></svg>',
                    desc: 'Bahasa pemrograman utama untuk pemrosesan data dan logika backend.'
                },
                {
                    id: 2,
                    name: 'FastAPI',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"></path></svg>',
                    desc: 'Framework performa tinggi untuk membangun API yang cepat dan efisien.'
                },
                {
                    id: 3,
                    name: 'Scikit-Learn',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>',
                    desc: 'Library machine learning untuk klasifikasi sentimen yang akurat.'
                },
                {
                    id: 4,
                    name: 'Selenium',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>',
                    desc: 'Otomatisasi browser untuk pengambilan data (scraping) komentar Instagram.'
                },
                {
                    id: 5,
                    name: 'Vue.js 3',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 14H4L12 2z"></path><path d="M12 8l4 7H8l4-7z"></path></svg>',
                    desc: 'Framework frontend modern untuk antarmuka pengguna yang reaktif.'
                },
                {
                    id: 6,
                    name: 'Tailwind CSS',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg>',
                    desc: 'Styling utilitas untuk membangun desain yang responsif dan estetis.'
                },
                {
                    id: 7,
                    name: 'Chart.js',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path><path d="M22 12A10 10 0 0 0 12 2v10z"></path></svg>',
                    desc: 'Visualisasi data melalui grafik yang interaktif dan mudah dipahami.'
                },
                {
                    id: 8,
                    name: 'Axios',
                    logo: '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"></path></svg>',
                    desc: 'Library HTTP client untuk komunikasi data antara frontend dan backend.'
                }
            ],
            articleItems: [
                {
                    id: 1,
                    title : 'Analisis Sentimen Terhadap Ulasan Pengguna Aplikasi Threads Instagram di Playstore Menggunakan Naive Bayes',
                    writer: 'Lukmana, L. O.',
                    desc  : 'Penelitian ini bertujuan untuk mengklasifikasi Review Pengguna Aplikasi Threads di PlayStore menjadi 2 sentimen yaitu positif dan negatif.',
                    link  : 'https://doi.org/10.23960/jitet.v13i2.6250'
                },
                {
                    id: 2,
                    title : 'Sentiment Analysis of Movie Reviews using Hybrid Method of Naive Bayes and Genetic Algorithm',
                    writer: 'Govindarajam, M.',
                    desc  : 'The ensemble framework is applied to sentiment classification tasks, with the aim of efficiently integrating different feature sets and classification algorithms to synthesize a more accurate classification procedure.',
                    link  : 'https://www.proquest.com/openview/6753aa944962d2f75944880f1f6c690e/1?pq-origsite=gscholar&cbl=1626343'
                },
                {
                    id: 3,
                    title : 'Sentiment Analysis on Social Media Againts Public Policy Using Multinomial Naive Bayes',
                    writer: 'Zulfikar, <i>et al</i>.',
                    desc  : 'The purpose of this study is to analyze text documents from Twitter about public policies in handling COVID-19 that are currently or have been determined. ',
                    link  : 'https://shura.shu.ac.uk/id/eprint/31645'
                }
            ],
            formData: {
                username: '',
                rangeMode: 'all',
                customRange: ''
            },
            isLoading: false,
            analysisResult: null,
            errorMessage: '',
        }
    },
    computed: {
        parsedSummary() {
            if (!this.analysisResult) return null;
            const summary = this.analysisResult.summary;
            return typeof summary === 'string' ? JSON.parse(summary) : summary;
        }
    },
    methods: {
        configureWindow() {
            this.isMobileMenuOpen = !this.isMobileMenuOpen;
        },

        async startAnalysis() {
            this.isLoading = true;
            this.analysisResult = null;
            this.errorMessage = '';

            const payload = new FormData();
            payload.append('username', this.formData.username);
            payload.append('rangeMode', this.formData.rangeMode);
            payload.append('customRange', this.formData.customRange);

            try {
                const response = await axios.post('http://127.0.0.1:8000/analyze/instagram', payload);
                this.analysisResult = response.data;

                this.$nextTick(() => {
                    setTimeout(() => { this.renderChart(); }, 200);
                    setTimeout(() => { 
                        document.getElementById('result-section')?.scrollIntoView({ behavior: 'smooth' }); 
                    }, 300);
                });

            } catch (error) {
                this.handleError(error);
            } finally {
                this.isLoading = false;
            }
        },

        renderChart() {
            const canvas = document.getElementById('sentimentChart');
            if (!canvas) return;

            const ctx = canvas.getContext('2d');
            const data = this.parsedSummary;
            console.log("Data untuk Chart:", data);

            if (!data) return;
            if (window.myChart) window.myChart.destroy();

            window.myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Positive', 'Neutral', 'Negative'],
                    datasets: [{
                        data: [
                            data.positive.count, 
                            data.neutral.count, 
                            data.negative.count
                        ],
                        backgroundColor: ['#238823', '#ffbf00', '#d2222d'],
                        borderWidth: 0,
                        hoverOffset: 10
                    }]
                },
                options: {
                    cutout: '60%',
                    plugins: { 
                        legend: { display: false } 
                    }
                }
            });
        },

        getBgColor(key) {
            if (key === 'positive') return 'bg-[#238823]/10';
            if (key === 'negative') return 'bg-[#d2222d]/10';
            return 'bg-[#ffbf00]/15';
        },

        getBarColor(key) {
            if (key === 'positive') return 'bg-[#238823]';
            if (key === 'negative') return 'bg-[#d2222d]';
            return 'bg-[#ffbf00]';
        },

        handleError(error) {
            if (error.response) {
                const data = error.response.data;
                this.errorMessage = typeof data.detail === 'object' 
                    ? JSON.stringify(data.detail) 
                    : (data.detail || "Terjadi kesalahan pada server.");
            } else {
                this.errorMessage = "Tidak bisa terhubung ke server. Pastikan Backend (FastAPI) sudah aktif.";
            }
            console.error("Analysis Error:", error);
            alert("Kendala: " + this.errorMessage);
        }
    }
}).mount('#app');