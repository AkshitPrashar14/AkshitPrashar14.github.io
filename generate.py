import os

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akshit Prashar | {title}</title>
    <link href="{font_url}" rel="stylesheet">
    <style>
        {css}
    </style>
</head>
<body>
    {bg_elements}
    <div class="container">
        {hero}
        
        <section class="section about">
            <h2>About Me</h2>
            <p>Hello! I'm <strong>Akshit Prashar</strong>, a Fourth-year Computer Science Engineering student specializing in Artificial Intelligence & Machine Learning.</p>
            <p>I love building products that combine Artificial Intelligence with robust backend engineering. Over the last year I've worked on multiple AI systems, backend applications, distributed systems, and cloud-native projects.</p>
            <p>I'm currently focused on becoming a Software Engineer capable of building production-scale applications that are performant, scalable and enjoyable to use.</p>
        </section>

        <section class="section skills">
            <h2>Technical Skills</h2>
            <div class="tags">
                <span class="tag">Java</span>
                <span class="tag">Python</span>
                <span class="tag">Spring Boot</span>
                <span class="tag">Node.js</span>
                <span class="tag">FastAPI</span>
                <span class="tag">TensorFlow</span>
                <span class="tag">Transformers / RAG</span>
                <span class="tag">PostgreSQL / Redis</span>
                <span class="tag">Docker</span>
                <span class="tag">Kubernetes</span>
            </div>
        </section>

        <section class="section projects">
            <h2>Featured Projects</h2>
            <div class="grid">
                <div class="card">
                    <h3>AI Mock Interview Platform</h3>
                    <p>A production-ready AI Interview Platform where candidates participate in realistic voice interviews. Performs speech-to-text, real-time evaluation, and feedback generation.</p>
                    <p><strong>Tech:</strong> Spring Boot, PostgreSQL, WebSockets, Whisper</p>
                </div>
                <div class="card">
                    <h3>AI Resume Analyzer</h3>
                    <p>An intelligent ATS-style Resume Parser that extracts education, skills, and experience, generating insights using Transformer models and LLMs.</p>
                    <p><strong>Tech:</strong> Python, FastAPI, Gemini, RAG</p>
                </div>
                <div class="card">
                    <h3>Govt QA System</h3>
                    <p>Semantic search QA platform trained over 88k+ government records. Combines semantic search, dense vector retrieval, and BERT QA.</p>
                    <p><strong>Tech:</strong> SBERT, FAISS, BERT, Python</p>
                </div>
                <div class="card">
                    <h3>Smart Parking Detection</h3>
                    <p>Computer Vision application capable of detecting empty and occupied parking slots using Convolutional Neural Networks.</p>
                    <p><strong>Tech:</strong> TensorFlow, Keras, CNN, OpenCV</p>
                </div>
                <div class="card">
                    <h3>Scalable URL Shortener</h3>
                    <p>Production-inspired distributed backend application implementing caching, containers, orchestration, and CI/CD pipelines.</p>
                    <p><strong>Tech:</strong> Node.js, Redis, Docker, Kubernetes, Terraform</p>
                </div>
            </div>
        </section>

        <section class="section contact">
            <h2>Let's Connect</h2>
            <p>I'm currently looking for Software Engineering, Backend Development, and AI opportunities. If you're building something exciting, I'd love to contribute.</p>
            <div class="links">
                <a href="mailto:yourmail@gmail.com" class="btn">Email</a>
                <a href="https://linkedin.com" class="btn">LinkedIn</a>
                <a href="https://github.com/AkshitPrashar14" class="btn">GitHub</a>
            </div>
        </section>
    </div>
</body>
</html>"""

themes = [
    {
        "id": 4,
        "title": "Glassmorphism",
        "font_url": "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', sans-serif; }
        body { background-color: #0f172a; color: white; min-height: 100vh; overflow-x: hidden; }
        .aurora { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 15% 50%, rgba(79,70,229,0.3), transparent 30%), radial-gradient(circle at 85% 30%, rgba(236,72,153,0.3), transparent 30%), radial-gradient(circle at 50% 80%, rgba(6,182,212,0.3), transparent 30%); filter: blur(60px); z-index: -1; }
        .container { max-width: 1000px; margin: 0 auto; padding: 40px 20px; }
        .hero { text-align: center; padding: 100px 0; }
        h1 { font-size: 4rem; font-weight: 800; margin-bottom: 20px; }
        h2 { font-size: 2.5rem; margin-bottom: 30px; font-weight: 600; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; }
        .hero p { font-size: 1.2rem; color: rgba(255,255,255,0.7); margin-bottom: 40px; }
        .section { margin-bottom: 80px; background: rgba(255,255,255,0.03); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 24px; padding: 50px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); }
        .section p { color: rgba(255,255,255,0.8); line-height: 1.8; margin-bottom: 15px; font-size: 1.1rem; }
        .tags { display: flex; flex-wrap: wrap; gap: 15px; }
        .tag { background: rgba(255,255,255,0.1); padding: 10px 20px; border-radius: 30px; font-weight: 300; border: 1px solid rgba(255,255,255,0.2); }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .card { background: rgba(0,0,0,0.2); padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.05); transition: 0.3s; }
        .card:hover { transform: translateY(-5px); background: rgba(255,255,255,0.08); }
        .card h3 { margin-bottom: 15px; color: #fff; font-size: 1.4rem; }
        .card p { color: rgba(255,255,255,0.6); font-size: 1rem; }
        .links { display: flex; gap: 20px; margin-top: 30px; }
        .btn { padding: 15px 30px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; border-radius: 30px; text-decoration: none; font-weight: 600; transition: 0.3s; }
        .btn:hover { background: rgba(255,255,255,0.2); transform: translateY(-3px); }
        """,
        "bg_elements": '<div class="aurora"></div>',
        "hero": '<div class="hero"><h1>Akshit Prashar</h1><p>Software Engineer crafting premium experiences & AI architectures</p></div>'
    },
    {
        "id": 5,
        "title": "Cyberpunk",
        "font_url": "https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Share Tech Mono', monospace; }
        body { background-color: #050505; color: #fff; min-height: 100vh; overflow-x: hidden; background-image: linear-gradient(0deg, transparent 24%, rgba(255,0,85,.1) 25%, rgba(255,0,85,.1) 26%, transparent 27%, transparent 74%, rgba(255,0,85,.1) 75%, rgba(255,0,85,.1) 76%, transparent 77%, transparent), linear-gradient(90deg, transparent 24%, rgba(255,0,85,.1) 25%, rgba(255,0,85,.1) 26%, transparent 27%, transparent 74%, rgba(255,0,85,.1) 75%, rgba(255,0,85,.1) 76%, transparent 77%, transparent); background-size: 50px 50px; }
        .container { max-width: 900px; margin: 0 auto; padding: 40px 20px; }
        .hero { text-align: center; padding: 80px 0; border-bottom: 2px dashed #ff0055; margin-bottom: 60px; }
        h1 { font-size: 4.5rem; color: #0ff; text-shadow: 0 0 10px #0ff; margin-bottom: 20px; text-transform: uppercase; }
        h2 { font-size: 2.5rem; color: #f0f; margin-bottom: 30px; text-shadow: 0 0 5px #f0f; text-transform: uppercase; border-bottom: 1px solid #333; padding-bottom: 10px; }
        p { color: #ddd; font-size: 1.1rem; line-height: 1.6; margin-bottom: 15px; }
        .section { margin-bottom: 80px; background: rgba(0,0,0,0.85); border: 1px solid #0ff; padding: 40px; box-shadow: 0 0 20px rgba(0,255,255,0.1); position: relative; }
        .section::before { content: 'SYS.MODULE'; position: absolute; top: -12px; left: 20px; background: #050505; color: #0ff; padding: 0 10px; font-size: 0.9rem; }
        .tags { display: flex; flex-wrap: wrap; gap: 15px; }
        .tag { background: #111; color: #ff0055; padding: 8px 15px; border: 1px solid #ff0055; text-transform: uppercase; font-size: 0.9rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .card { background: #0a0a0a; border-left: 4px solid #0ff; padding: 25px; transition: 0.2s; }
        .card:hover { background: #111; border-color: #ff0055; }
        .card h3 { color: #fff; margin-bottom: 10px; font-size: 1.4rem; text-shadow: 0 0 5px #fff; }
        .card p { color: #aaa; font-size: 0.95rem; }
        .links { display: flex; gap: 20px; margin-top: 30px; flex-wrap: wrap;}
        .btn { background: transparent; color: #ff0055; border: 2px solid #ff0055; padding: 12px 30px; font-size: 1.1rem; text-transform: uppercase; text-decoration: none; clip-path: polygon(10% 0, 100% 0, 100% 70%, 90% 100%, 0 100%, 0 30%); transition: 0.2s; }
        .btn:hover { background: #ff0055; color: #050505; box-shadow: 0 0 15px #ff0055; }
        """,
        "bg_elements": '',
        "hero": '<div class="hero"><h1>Akshit Prashar</h1><p>> NEURAL_LINK_ESTABLISHED :: AI_ENGINEER_ONLINE</p></div>'
    },
    {
        "id": 6,
        "title": "Claymorphism",
        "font_url": "https://fonts.googleapis.com/css2?family=Nunito:wght@600;800&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Nunito', sans-serif; }
        body { background: #E8F0FE; color: #444; min-height: 100vh; overflow-x: hidden; }
        .container { max-width: 1000px; margin: 0 auto; padding: 60px 20px; }
        .hero { text-align: center; margin-bottom: 80px; padding: 40px; }
        h1 { color: #536dfe; font-size: 3.5rem; margin-bottom: 15px; }
        h2 { color: #ff6b81; font-size: 2.2rem; margin-bottom: 30px; }
        p { color: #7f8fa6; font-size: 1.1rem; line-height: 1.7; margin-bottom: 15px; }
        .section { background: #E8F0FE; padding: 50px; border-radius: 40px; margin-bottom: 60px; box-shadow: 25px 25px 50px rgba(184,197,214,0.8), -20px -20px 40px #ffffff, inset 5px 5px 15px rgba(255,255,255,0.5), inset -5px -5px 15px rgba(184,197,214,0.2); }
        .tags { display: flex; flex-wrap: wrap; gap: 15px; }
        .tag { background: #E8F0FE; color: #536dfe; padding: 12px 25px; border-radius: 20px; font-weight: 800; box-shadow: 8px 8px 16px rgba(184,197,214,0.6), -8px -8px 16px #ffffff; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 35px; }
        .card { background: #E8F0FE; padding: 35px; border-radius: 30px; box-shadow: 15px 15px 30px rgba(184,197,214,0.7), -15px -15px 30px #ffffff; transition: 0.3s; }
        .card:hover { transform: scale(1.03); }
        .card h3 { color: #536dfe; margin-bottom: 15px; font-size: 1.4rem; }
        .card p { font-size: 1rem; color: #666; }
        .links { display: flex; gap: 20px; margin-top: 30px; flex-wrap: wrap; }
        .btn { background: #ff6b81; color: white; padding: 15px 35px; border-radius: 25px; text-decoration: none; font-size: 1.1rem; font-weight: 800; box-shadow: 8px 8px 16px rgba(255,107,129,0.4), inset 4px 4px 8px rgba(255,255,255,0.4), inset -4px -4px 8px rgba(200,40,60,0.4); transition: 0.2s; }
        .btn:hover { transform: translateY(-3px); }
        .btn:active { transform: translateY(2px); box-shadow: inset 6px 6px 12px rgba(200,40,60,0.4), inset -6px -6px 12px rgba(255,255,255,0.4); }
        """,
        "bg_elements": '',
        "hero": '<div class="hero section"><h1>Akshit Prashar</h1><p>Software Engineer & UX Enthusiast making soft, friendly tech.</p></div>'
    },
    {
        "id": 7,
        "title": "Bauhaus",
        "font_url": "https://fonts.googleapis.com/css2?family=Inter:wght@400;900&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background: #f4f4f0; color: #111; min-height: 100vh; overflow-x: hidden; }
        .container { display: grid; grid-template-columns: 1fr; border-left: 5px solid #111; border-right: 5px solid #111; max-width: 1200px; margin: 0 auto; background: #fff; }
        .hero { padding: 100px 50px; background: #e32626; color: #f4f4f0; border-bottom: 5px solid #111; position: relative; overflow: hidden; }
        h1 { font-size: clamp(4rem, 8vw, 8rem); font-weight: 900; line-height: 0.9; text-transform: uppercase; letter-spacing: -3px; margin-bottom: 20px; z-index: 2; position: relative; }
        h2 { font-size: 3rem; font-weight: 900; text-transform: uppercase; margin-bottom: 30px; letter-spacing: -1px; }
        p { font-size: 1.15rem; font-weight: 400; line-height: 1.6; max-width: 800px; margin-bottom: 15px;}
        .section { padding: 80px 50px; border-bottom: 5px solid #111; position: relative; }
        .about { background: #fff; }
        .skills { background: #f2ce18; }
        .projects { background: #2654e3; color: #fff; }
        .projects p { color: #fff; }
        .contact { background: #fff; }
        .tags { display: flex; flex-wrap: wrap; gap: 10px; }
        .tag { background: #111; color: #fff; padding: 15px 25px; font-weight: 900; text-transform: uppercase; font-size: 1.1rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 0; border: 5px solid #111; background: #111; }
        .card { background: #fff; color: #111; padding: 40px; position: relative; transition: 0.2s; border: 1px solid #111;}
        .card:hover { background: #f4f4f0; }
        .card h3 { font-size: 1.8rem; font-weight: 900; margin-bottom: 15px; text-transform: uppercase; }
        .card p { color: #111; font-size: 1rem; }
        .links { display: flex; gap: 20px; margin-top: 40px; flex-wrap: wrap;}
        .btn { background: #111; color: #fff; padding: 20px 40px; font-size: 1.2rem; font-weight: 900; text-transform: uppercase; text-decoration: none; border: none; cursor: pointer; transition: 0.2s; }
        .btn:hover { background: #e32626; }
        .circle { position: absolute; width: 300px; height: 300px; background: #2654e3; border-radius: 50%; right: -50px; bottom: -50px; z-index: 1; }
        """,
        "bg_elements": '',
        "hero": '<div class="hero"><h1>Akshit<br>Prashar</h1><p>ENGINEER // ARCHITECT // DEVELOPER</p><div class="circle"></div></div>'
    },
    {
        "id": 8,
        "title": "Retro OS",
        "font_url": "https://fonts.googleapis.com/css2?family=VT323&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'VT323', monospace; }
        body { background: #008080; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; display: flex; flex-direction: column; gap: 30px; }
        .section { background: #c0c0c0; border: 2px solid; border-color: #ffffff #808080 #808080 #ffffff; box-shadow: 2px 2px 0 #000; padding: 20px; position: relative;}
        .section::before { content: 'Win32_Subsystem'; position: absolute; top: -10px; left: 10px; background: #c0c0c0; padding: 0 5px; font-size: 1.2rem; font-weight: bold;}
        .hero { text-align: center; padding: 40px 20px; }
        h1 { font-size: 3.5rem; margin-bottom: 10px; }
        h2 { font-size: 2.2rem; margin-bottom: 20px; border-bottom: 2px groove #fff; padding-bottom: 5px; color: #000080; }
        p { font-size: 1.4rem; margin-bottom: 15px; line-height: 1.5; color: #000; }
        .tags { display: flex; flex-wrap: wrap; gap: 10px; }
        .tag { background: #fff; border: 2px inset #fff; padding: 5px 15px; font-size: 1.3rem; color: #000; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .card { background: #fff; border: 2px inset #fff; padding: 15px; }
        .card h3 { font-size: 1.6rem; color: #000080; margin-bottom: 10px; }
        .links { display: flex; gap: 15px; margin-top: 20px; flex-wrap: wrap;}
        .btn { background: #c0c0c0; border: 2px solid; border-color: #ffffff #808080 #808080 #ffffff; padding: 8px 25px; font-size: 1.3rem; text-decoration: none; color: black; display: inline-block; cursor: pointer; box-shadow: 1px 1px 0 #000; }
        .btn:active { border-color: #808080 #ffffff #ffffff #808080; box-shadow: none; padding: 9px 24px 7px 26px; }
        """,
        "bg_elements": '',
        "hero": '<div class="section hero"><h1>AKSHIT PRASHAR</h1><p>System Booted. Engineer ready for deployment.</p></div>'
    },
    {
        "id": 9,
        "title": "Dark Luxury",
        "font_url": "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Lato:wght@300;400&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #050505; color: #f2f2f2; font-family: 'Lato', sans-serif; overflow-x: hidden; }
        .container { max-width: 1000px; margin: 0 auto; padding: 0 40px; }
        .hero { padding: 120px 0 80px; border-bottom: 1px solid rgba(212, 175, 55, 0.2); margin-bottom: 80px; text-align: center; }
        h1, h2 { font-family: 'Playfair Display', serif; font-weight: 400; }
        h1 { font-size: 5rem; margin-bottom: 20px; }
        h1 span { font-style: italic; color: #d4af37; }
        h2 { font-size: 2.5rem; margin-bottom: 40px; color: #d4af37; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px; }
        p { font-size: 1.1rem; line-height: 1.8; color: #aaa; margin-bottom: 20px; font-weight: 300; }
        .section { margin-bottom: 100px; }
        .tags { display: flex; flex-wrap: wrap; gap: 20px; }
        .tag { border-bottom: 1px solid #d4af37; padding-bottom: 5px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; color: #fff; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 50px; }
        .card { padding-bottom: 30px; border-bottom: 1px solid rgba(255,255,255,0.1); transition: 0.4s; }
        .card:hover { border-bottom-color: #d4af37; transform: translateY(-5px); }
        .card h3 { font-family: 'Playfair Display', serif; font-size: 1.6rem; margin-bottom: 15px; color: #fff; }
        .card p { font-size: 0.95rem; }
        .links { display: flex; gap: 30px; margin-top: 40px; flex-wrap: wrap;}
        .btn { text-decoration: none; color: #d4af37; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 3px; border-bottom: 1px solid #d4af37; padding-bottom: 8px; transition: 0.4s; }
        .btn:hover { color: #fff; border-bottom-color: #fff; }
        """,
        "bg_elements": '',
        "hero": '<div class="hero"><h1>Akshit<br><span>Prashar</span></h1><p style="text-transform:uppercase; letter-spacing:5px;">Est. 2026 // Premium Engineering</p></div>'
    },
    {
        "id": 10,
        "title": "Organic",
        "font_url": "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600&family=Montserrat:wght@300;400&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #f5f1e7; color: #4a5d4e; font-family: 'Montserrat', sans-serif; overflow-x: hidden; }
        .blob-bg { position: fixed; width: 100vw; height: 100vh; background: #e2dfcf; border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; opacity: 0.5; animation: morph 12s ease-in-out infinite alternate; z-index: -1; top: -20vh; left: -10vw; }
        @keyframes morph { 0% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; } 100% { border-radius: 60% 40% 30% 70% / 50% 60% 40% 60%; transform: scale(1.1) rotate(5deg); } }
        .container { max-width: 900px; margin: 0 auto; padding: 60px 20px; position: relative; z-index: 1; }
        .hero { text-align: center; margin-bottom: 80px; padding-top: 50px; }
        h1, h2, h3 { font-family: 'Cormorant Garamond', serif; color: #3b4d3f; }
        h1 { font-size: 5rem; margin-bottom: 20px; }
        h2 { font-size: 3rem; margin-bottom: 30px; text-align: center; border-bottom: 1px solid rgba(119,143,123,0.3); padding-bottom: 15px;}
        p { font-size: 1.1rem; line-height: 1.8; color: #6a7c6e; margin-bottom: 20px; }
        .section { margin-bottom: 80px; background: rgba(255,255,255,0.6); padding: 50px; border-radius: 30px 10px 30px 10px; border: 1px solid rgba(119,143,123,0.2); }
        .tags { display: flex; flex-wrap: wrap; gap: 15px; justify-content: center; }
        .tag { background: rgba(255,255,255,0.6); padding: 12px 25px; border-radius: 30px 10px 30px 10px; border: 1px solid #778f7b; color: #3b4d3f; font-weight: 400; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; }
        .card { background: rgba(255,255,255,0.8); padding: 35px; border-radius: 20px 50px 20px 50px; border: 1px solid rgba(119,143,123,0.3); transition: 0.4s; }
        .card:hover { background: #fff; border-radius: 50px 20px 50px 20px; box-shadow: 0 10px 30px rgba(74,93,78,0.1); }
        .card h3 { font-size: 1.8rem; margin-bottom: 15px; }
        .card p { font-size: 0.95rem; }
        .links { display: flex; gap: 20px; justify-content: center; margin-top: 40px; flex-wrap: wrap;}
        .btn { text-decoration: none; background: #778f7b; color: white; padding: 15px 35px; border-radius: 30px 10px 30px 10px; transition: 0.4s; font-size: 1rem; letter-spacing: 1px; }
        .btn:hover { background: #4a5d4e; border-radius: 10px 30px 10px 30px; }
        """,
        "bg_elements": '<div class="blob-bg"></div>',
        "hero": '<div class="hero"><h1>Akshit Prashar</h1><p>Crafting digital experiences that feel natural, fluid, and profoundly human.</p></div>'
    },
    {
        "id": 11,
        "title": "Cosmic",
        "font_url": "https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&display=swap",
        "css": """
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Rajdhani', sans-serif; }
        body { background: #020111; color: white; min-height: 100vh; overflow-x: hidden; }
        .space { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at bottom, #1b2735 0%, #090a0f 100%); z-index: -2; }
        .stars { width: 1px; height: 1px; background: transparent; position: fixed; z-index: -1; box-shadow: 10vw 20vh #fff, 30vw 50vh #fff, 80vw 80vh #fff, 20vw 90vh #fff, 60vw 10vh #fff, 90vw 40vh #fff, 40vw 30vh #fff, 70vw 70vh #fff, 15vw 60vh #fff, 50vw 85vh #fff; animation: animStar 50s linear infinite; }
        @keyframes animStar { from { transform: translateY(0px); } to { transform: translateY(-100vh); } }
        .container { max-width: 1000px; margin: 0 auto; padding: 60px 20px; }
        .hero { text-align: center; margin-bottom: 80px; padding: 60px 40px; background: rgba(118,169,255,0.05); border-radius: 30px; box-shadow: 0 0 100px rgba(118,169,255,0.1); border: 1px solid rgba(118,169,255,0.2); }
        h1 { font-size: 5rem; letter-spacing: 5px; text-transform: uppercase; text-shadow: 0 0 20px rgba(118,169,255,0.5); margin-bottom: 15px; }
        h2 { font-size: 2.2rem; letter-spacing: 3px; color: #a4c8ff; margin-bottom: 25px; text-transform: uppercase; border-bottom: 1px solid rgba(118,169,255,0.2); padding-bottom: 10px; }
        p { font-size: 1.2rem; letter-spacing: 1px; color: #d0e1ff; line-height: 1.6; margin-bottom: 15px; }
        .section { margin-bottom: 60px; background: rgba(10,15,30,0.6); border: 1px solid rgba(118,169,255,0.2); padding: 40px; border-radius: 20px; backdrop-filter: blur(10px); }
        .tags { display: flex; flex-wrap: wrap; gap: 15px; }
        .tag { background: transparent; border: 1px solid #76a9ff; color: #a4c8ff; padding: 8px 20px; border-radius: 50px; font-size: 1.1rem; box-shadow: inset 0 0 10px rgba(118,169,255,0.2); }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .card { background: rgba(255,255,255,0.02); padding: 30px; border-radius: 15px; border-top: 1px solid rgba(118,169,255,0.3); transition: 0.3s; }
        .card:hover { background: rgba(118,169,255,0.1); box-shadow: 0 -10px 30px rgba(118,169,255,0.1); }
        .card h3 { color: #fff; font-size: 1.5rem; margin-bottom: 15px; }
        .card p { font-size: 1rem; }
        .links { display: flex; gap: 20px; margin-top: 30px; flex-wrap: wrap; }
        .btn { text-decoration: none; color: #fff; border: 1px solid #76a9ff; padding: 12px 35px; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase; border-radius: 50px; box-shadow: 0 0 15px rgba(118,169,255,0.3), inset 0 0 10px rgba(118,169,255,0.2); transition: 0.3s; }
        .btn:hover { background: #76a9ff; color: #020111; box-shadow: 0 0 30px #76a9ff; }
        """,
        "bg_elements": '<div class="space"></div><div class="stars"></div>',
        "hero": '<div class="hero"><h1>Akshit Prashar</h1><p>ENGINEERING THE FUTURE</p></div>'
    }
]

import json
for t in themes:
    html = base_html.format(
        title=t["title"],
        font_url=t["font_url"],
        css=t["css"],
        bg_elements=t["bg_elements"],
        hero=t["hero"]
    )
    with open(f"c:\\Users\\HP\\Desktop\\Portfolio\\index{t['id']}.html", "w", encoding="utf-8") as f:
        f.write(html)

print("Generated 8 html files")
