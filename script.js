// --- THREE.JS DYNAMIC SCENE SETUP ---
        const canvas = document.getElementById('bg-canvas');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0xF4F6F6, 0.05);
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
        camera.position.set(0, 0, 15);

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.9);
        scene.add(ambientLight);
        const dirLight = new THREE.DirectionalLight(0xffeedd, 1.2);
        dirLight.position.set(5, 5, 5);
        scene.add(dirLight);

        // Main Material
        const material = new THREE.MeshStandardMaterial({
            color: 0x29363D, roughness: 0.7, metalness: 0.2, flatShading: true
        });

        // 1. Curiosity (Orbital Gyroscope for Introduction)
        const meshCuriosity = new THREE.Group();
        for (let i = 0; i < 3; i++) {
            const ring = new THREE.Mesh(new THREE.TorusGeometry(3.5, 0.15, 16, 100), material);
            ring.rotation.x = Math.random() * Math.PI;
            ring.rotation.y = Math.random() * Math.PI;
            meshCuriosity.add(ring);
        }

        // 2. Adaptability (Smooth Halo Torus for Experience)
        const meshAdaptability = new THREE.Mesh(new THREE.TorusGeometry(3.5, 1.2, 64, 100), material);

        // 3. Quick Learning (Icosahedron Crystal for Collection)
        const meshLearning = new THREE.Mesh(new THREE.IcosahedronGeometry(3.5, 0), material);

        // 4. Hunger (Floating Monolith Octahedron for Contact)
        const meshHunger = new THREE.Mesh(new THREE.OctahedronGeometry(3, 0), material);
        meshHunger.scale.y = 1.6; // Stretch it into a tall diamond

        // Master Group
        const sculptureGroup = new THREE.Group();
        sculptureGroup.add(meshCuriosity);
        sculptureGroup.add(meshAdaptability);
        sculptureGroup.add(meshLearning);
        sculptureGroup.add(meshHunger);

        // Set Initial Visibility
        meshAdaptability.visible = false;
        meshLearning.visible = false;
        meshHunger.visible = false;

        sculptureGroup.position.x = window.innerWidth > 900 ? 5 : 0;
        scene.add(sculptureGroup);

        // --- SPA ROUTING & SHAPE SWAPPING ---
        const navLinks = document.querySelectorAll('.nav-link');
        const pages = document.querySelectorAll('.page');

        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                navLinks.forEach(l => l.classList.remove('active'));
                pages.forEach(p => p.classList.remove('active'));
                link.classList.add('active');

                const targetId = link.getAttribute('data-target');
                document.getElementById(targetId).classList.add('active');
                window.scrollTo({ top: 0, behavior: 'smooth' });

                // Swap the 3D Object Based on Page
                meshCuriosity.visible = false;
                meshAdaptability.visible = false;
                meshLearning.visible = false;
                meshHunger.visible = false;

                if (targetId === 'home') meshCuriosity.visible = true;
                if (targetId === 'about') meshAdaptability.visible = true;
                if (targetId === 'projects') meshLearning.visible = true;
                if (targetId === 'contact') meshHunger.visible = true;
            });
        });

        // --- DYNAMIC THEME ENGINE ---
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('change', (e) => {
                const isDark = e.target.checked;
                if(isDark) document.body.classList.add('theme-dark');
                else document.body.classList.remove('theme-dark');

                // Update Three.js Colors
                setTimeout(() => {
                    const style = getComputedStyle(document.body);
                    const meshColor = parseInt(style.getPropertyValue('--mesh-color').trim(), 16);
                    const fogColor = parseInt(style.getPropertyValue('--fog-color').trim(), 16);

                    material.color.setHex(meshColor);
                    scene.fog.color.setHex(fogColor);
                    material.wireframe = false;
                }, 50);
            });
        }

        // --- PARALLAX & ANIMATION LOOP ---
        let mouseX = 0, mouseY = 0;
        const windowHalfX = window.innerWidth / 2, windowHalfY = window.innerHeight / 2;
        document.addEventListener('mousemove', (e) => {
            mouseX = (e.clientX - windowHalfX) * 0.001;
            mouseY = (e.clientY - windowHalfY) * 0.001;
        });

        let scrollY = 0;
        window.addEventListener('scroll', () => { scrollY = window.scrollY * 0.005; });

        const clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            const time = clock.getElapsedTime();

            // Base slow rotation for whatever object is active
            sculptureGroup.rotation.y = time * 0.1;
            sculptureGroup.rotation.x = time * 0.05;

            // Specific internal rotations
            if (meshCuriosity.visible) {
                meshCuriosity.children[0].rotation.x += 0.01;
                meshCuriosity.children[1].rotation.y += 0.015;
                meshCuriosity.children[2].rotation.z += 0.02;
            }

            camera.position.x += (mouseX - camera.position.x) * 0.05;
            camera.position.y += (-mouseY - scrollY - camera.position.y) * 0.05;
            camera.lookAt(scene.position);
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            sculptureGroup.position.x = window.innerWidth > 900 ? 5 : 0;
        });

        // --- AI CHATBOT (GUARDRAILS ACTIVE) ---
        const chatBtn = document.getElementById('ai-chat-btn');
        const chatWindow = document.getElementById('ai-chat-window');
        const closeChat = document.getElementById('close-chat');
        const chatInput = document.getElementById('chat-input-field');
        const sendBtn = document.getElementById('send-chat');
        const messagesDiv = document.getElementById('chat-messages');

        const mockAIResponses = {
            "skills": "Akshit is highly proficient in Java, Spring Boot, Python, FastAPI, TensorFlow, and Docker. He specializes in Backend and ML.",
            "projects": "His top projects include an AI Mock Interview Platform (Spring Boot & Whisper) and an AI Resume Analyzer utilizing LLMs and RAG.",
            "experience": "He's a 4th-year CS Engineering student heavily focused on AI integration and scalable backend systems.",
            "contact": "You can reach him via email or connect with him on LinkedIn!"
        };

        const guardrailMessage = "I am strictly programmed to only answer questions related to Akshit's professional background, skills, and projects.";

        function addMessage(text, sender) {
            const msg = document.createElement('div');
            msg.className = `msg ${sender}`;
            msg.textContent = text;
            messagesDiv.appendChild(msg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        async function handleChatSubmit() {
            const userText = chatInput.value.trim();
            if (!userText) return;
            addMessage(userText, 'user');
            chatInput.value = '';

            const typingIndicator = document.createElement('div');
            typingIndicator.className = 'msg ai';
            typingIndicator.textContent = 'Typing...';
            messagesDiv.appendChild(typingIndicator);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;

            try {
                const response = await fetch('https://portfolio-chatbot-api-htnq.onrender.com/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: userText })
                });
                const data = await response.json();
                messagesDiv.removeChild(typingIndicator);
                addMessage(data.reply || "Sorry, no response.", 'ai');
            } catch (error) {
                messagesDiv.removeChild(typingIndicator);
                addMessage("Sorry, the AI backend is currently offline.", 'ai');
            }
        }

        chatBtn.addEventListener('click', () => { chatWindow.classList.add('open'); chatBtn.style.display = 'none'; });
        closeChat.addEventListener('click', () => { chatWindow.classList.remove('open'); chatBtn.style.display = 'block'; });
        sendBtn.addEventListener('click', handleChatSubmit);
        chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') handleChatSubmit(); });

        // --- PROJECT MODAL LOGIC ---
        const projectsData = {
            "mock-interview": {
                title: "AI Mock Interview Platform",
                desc: "A production-ready voice interview platform with real-time AI evaluation and conversational management. Built to simulate realistic technical and behavioral interviews with dynamic feedback and scoring.",
                tech: "Spring Boot • PostgreSQL • Whisper",
                link: "https://github.com/AkshitPrashar14/AI-Mock-Interview-Platform",
                img: "assets/arch_mock_interview.png"
            },
            "operator-console": {
                title: "Operator Console",
                desc: "A centralized operations dashboard and management console for streamlined monitoring and control. Provides real-time metrics, system health tracking, and operational overrides for distributed microservices.",
                tech: "React • Node.js • Dashboard",
                link: "https://operator-console-24kqeqfst-akshitprashar14s-projects.vercel.app/",
                img: "assets/arch_operator_console.png"
            },
            "resume-intelligence": {
                title: "AI Resume Intelligence",
                desc: "An intelligent ATS-style parser utilizing Transformer models to distill complex insights via LLMs. Extracts education, parses implicit skills, and scores candidates against job descriptions automatically.",
                tech: "Python • FastAPI • Gemini",
                link: "https://ai-powered-resume-intelligence-platform-d5n16voct.vercel.app/",
                img: "assets/arch_resume_intelligence.png"
            },
            "typeform": {
                title: "Typeform Repo",
                desc: "A dynamic, interactive form builder platform inspired by Typeform with complex state management. Supports conditional logic branching, real-time validation, and elegant block-by-block transitions.",
                tech: "React • State Management • UI/UX",
                link: "https://typeform-repo.vercel.app/",
                img: "assets/arch_typeform.png"
            },
            "webscrapper": {
                title: "Webscapper",
                desc: "A robust data extraction tool designed to efficiently scrape, parse, and store web information. Implements headless browsing, proxy rotation, and asynchronous request handling for large-scale crawling.",
                tech: "Python • BeautifulSoup • Data Engineering",
                link: "https://acydon-assignment.onrender.com/",
                img: "assets/arch_webscrapper.png"
            },
            "db-indexer": {
                title: "Autonomous DB Indexer",
                desc: "An intelligent database utility that autonomously analyzes query patterns to generate optimal indexes. Hooks into PostgreSQL execution plans to recommend and apply performance-enhancing structures.",
                tech: "Python • PostgreSQL • Redis",
                link: "https://github.com/AkshitPrashar14/Autonomous-DB-Indexer",
                img: "assets/arch_db_indexer.png"
            },
            "openenv": {
                title: "OpenENV RL Project",
                desc: "An open reinforcement learning environment for training and evaluating autonomous AI agents. Built on top of Gym, offering configurable physics and observation spaces for advanced ML research.",
                tech: "Python • Reinforcement Learning • Gym",
                link: "https://github.com/AkshitPrashar14/OpenENV-RL-Project",
                img: "assets/arch_openenv.png"
            }
        };

        function openProjectModal(id) {
            const data = projectsData[id];
            document.getElementById('modal-title').innerText = data.title;
            document.getElementById('modal-desc').innerText = data.desc;
            document.getElementById('modal-tech').innerText = data.tech;
            document.getElementById('modal-link').href = data.link;
            document.getElementById('modal-img').style.backgroundImage = `url('${data.img}')`;
            
            const modal = document.getElementById('project-modal');
            modal.style.display = 'flex';
            setTimeout(() => modal.classList.add('active'), 10);
        }

        function closeProjectModal() {
            const modal = document.getElementById('project-modal');
            modal.classList.remove('active');
            setTimeout(() => modal.style.display = 'none', 300);
        }