TEMPLATES = {
    "Simple Home Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Elegant Concept | Minimalist Landing Page</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --primary: #1a1a1a;
            --accent: #7c6a5a;
            --bg: #fdfcfb;
            --text-muted: #666;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--primary);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* --- Navigation --- */
        nav {
            padding: 2rem 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: absolute;
            width: 100%;
            z-index: 10;
        }

        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            font-weight: 700;
            letter-spacing: -1px;
        }

        .nav-links {
            display: flex;
            gap: 2.5rem;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--primary);
            font-size: 0.9rem;
            font-weight: 400;
            transition: var(--transition);
            opacity: 0.7;
        }

        .nav-links a:hover {
            opacity: 1;
            letter-spacing: 1px;
        }

        /* --- Hero Section --- */
        .hero {
            height: 100vh;
            display: flex;
            align-items: center;
            padding: 0 10%;
            background: radial-gradient(circle at 80% 20%, #f3efec 0%, transparent 40%);
        }

        .hero-content {
            max-width: 600px;
            animation: fadeInUp 1s ease-out;
        }

        .hero-content h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(3rem, 8vw, 5rem);
            line-height: 1.1;
            margin-bottom: 1.5rem;
        }

        .hero-content p {
            font-size: 1.1rem;
            color: var(--text-muted);
            margin-bottom: 2.5rem;
            max-width: 400px;
        }

        /* --- Buttons --- */
        .btn {
            display: inline-block;
            padding: 1rem 2.5rem;
            background: var(--primary);
            color: white;
            text-decoration: none;
            border-radius: 0;
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: var(--transition);
            border: 1px solid var(--primary);
        }

        .btn:hover {
            background: transparent;
            color: var(--primary);
            transform: translateY(-3px);
        }

        /* --- Features Section --- */
        .features {
            padding: 8rem 10%;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 4rem;
        }

        .feature-card {
            opacity: 0;
            transform: translateY(30px);
            transition: var(--transition);
        }

        .feature-card.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .feature-card h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .feature-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        /* --- Animations --- */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            nav { padding: 2rem 5%; }
            .nav-links { display: none; }
            .hero { padding: 0 5%; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="logo">AESTHETE.</div>
        <ul class="nav-links">
            <li><a href="#">Process</a></li>
            <li><a href="#">Works</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <h1>Curation of Fine Design.</h1>
            <p>A minimalist approach to building digital experiences that resonate and endure.</p>
            <a href="#" class="btn">Explore More</a>
        </div>
    </section>

    <section class="features" id="scroll-target">
        <div class="feature-card">
            <h3>Purpose</h3>
            <p>We believe every pixel should serve a function. No clutter, just clarity and intentionality.</p>
        </div>
        <div class="feature-card">
            <h3>Craft</h3>
            <p>Hand-coded experiences tailored to the unique voice of your brand or personal identity.</p>
        </div>
        <div class="feature-card">
            <h3>Longevity</h3>
            <p>Trends fade, but clean typography and balanced whitespace are timeless assets.</p>
        </div>
    </section>

    <script>
        // Simple Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.2
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.feature-card').forEach(card => {
            observer.observe(card);
        });
    </script>
</body>
</html>""",
    "Simple Home Page with Mobile Optimized Nav Buttons and Footer": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aesthete | Premium Template</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --primary: #1a1a1a;
            --accent: #7c6a5a;
            --bg: #fdfcfb;
            --text-muted: #888;
            --transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--primary);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }

        /* --- NAVIGATION --- */
        nav {
            padding: 2.5rem 10%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            background: rgba(253, 252, 251, 0.8);
            backdrop-filter: blur(10px);
        }

        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.4rem;
            font-weight: 700;
            z-index: 1001; /* Stay above mobile menu */
        }

        .nav-links {
            display: flex;
            gap: 3rem;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--primary);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: var(--transition);
        }

        /* --- MOBILE MENU (HIDDEN BY DEFAULT) --- */
        .menu-toggle {
            display: none;
            flex-direction: column;
            gap: 6px;
            cursor: pointer;
            z-index: 1001;
        }

        .menu-toggle span {
            width: 25px;
            height: 2px;
            background: var(--primary);
            transition: var(--transition);
        }

        /* --- HERO & CONTENT --- */
        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 0 10%;
        }

        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 10vw, 6rem);
            line-height: 1;
            margin-bottom: 2rem;
        }

        /* --- FOOTER --- */
        footer {
            padding: 4rem 10%;
            border-top: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .footer-links {
            display: flex;
            gap: 2rem;
        }

        .footer-links a {
            color: var(--text-muted);
            text-decoration: none;
        }

        /* --- MOBILE RESPONSIVENESS --- */
        @media (max-width: 768px) {
            .menu-toggle { display: flex; }

            .nav-links {
                position: fixed;
                top: 0;
                right: -100%;
                height: 100vh;
                width: 70%;
                background: white;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                transition: var(--transition);
                box-shadow: -10px 0 30px rgba(0,0,0,0.05);
            }

            .nav-links.active { right: 0; }

            /* Toggle Animation */
            .active-toggle span:nth-child(1) { transform: translateY(8px) rotate(45deg); }
            .active-toggle span:nth-child(2) { opacity: 0; }
            .active-toggle span:nth-child(3) { transform: translateY(-8px) rotate(-45deg); }
            
            footer {
                flex-direction: column;
                gap: 2rem;
                text-align: center;
            }
        }
    </style>
</head>
<body>

    <nav>
        <div class="logo">AESTHETE.</div>
        
        <div class="menu-toggle" id="mobile-menu">
            <span></span>
            <span></span>
            <span></span>
        </div>

        <ul class="nav-links" id="nav-list">
            <li><a href="#work">Work</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section class="hero">
        <h1>Simplicity is the ultimate sophistication.</h1>
        <p style="color: var(--text-muted); max-width: 500px;">Helping visionaries build digital legacies through intentional design and refined code.</p>
    </section>

    <footer>
        <div>&copy; 2026 AESTHETE STUDIO</div>
        <div class="footer-links">
            <a href="#">Instagram</a>
            <a href="#">LinkedIn</a>
            <a href="#">Twitter</a>
        </div>
    </footer>

    <script>
        const menuToggle = document.getElementById('mobile-menu');
        const navList = document.getElementById('nav-list');

        menuToggle.addEventListener('click', () => {
            navList.classList.toggle('active');
            menuToggle.classList.toggle('active-toggle');
        });

        // Close menu when a link is clicked
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navList.classList.remove('active');
                menuToggle.classList.remove('active-toggle');
            });
        });
    </script>
</body>
</html>""",
    "Simple Dashboard Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleek OS | Professional Architecture</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <style>
        :root {
            /* Palette: Pure Neutral */
            --bg: #fcfcfc;
            --surface: #ffffff;
            --border: #eeeeee;
            --black: #000000;
            --dark-gray: #111111;
            --muted: #888888;
            --accent-soft: #f5f5f5;
            
            --sidebar-width: 260px;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        /* Base Reset */
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--dark-gray);
            display: flex;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }

        /* --- SIDEBAR NAVIGATION --- */
        aside {
            width: var(--sidebar-width);
            background: var(--surface);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
            z-index: 1000;
            transition: var(--transition);
        }

        .brand-area {
            padding: 3.5rem 2rem;
            font-weight: 600;
            font-size: 0.85rem;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: var(--black);
        }

        .nav-container {
            flex-grow: 1;
            padding: 0 1.2rem;
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 0.9rem 1.2rem;
            color: var(--muted);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            margin-bottom: 4px;
            transition: var(--transition);
            border-radius: 2px;
        }

        .nav-link:hover {
            color: var(--black);
            background: var(--accent-soft);
        }

        .nav-link.active {
            background: var(--black);
            color: var(--surface);
        }

        /* --- MAIN VIEWPORT --- */
        main {
            margin-left: var(--sidebar-width);
            flex-grow: 1;
            padding: 4rem 6%;
            max-width: 1600px;
            transition: var(--transition);
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 4rem;
        }

        .view-title h1 {
            font-size: 1.8rem;
            font-weight: 600;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
        }

        .view-title p {
            font-size: 0.85rem;
            color: var(--muted);
        }

        /* Mobile Trigger */
        .menu-trigger {
            display: none;
            cursor: pointer;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 10px 20px;
            border: 1px solid var(--black);
            background: transparent;
        }

        /* --- THE DASHBOARD GRID --- */
        .layout-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .module {
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 2.5rem;
            transition: var(--transition);
        }

        .module:hover {
            border-color: var(--black);
            transform: translateY(-2px);
        }

        .module-header {
            font-size: 0.65rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--muted);
            margin-bottom: 2.5rem;
            display: block;
        }

        .module-content .value {
            font-size: 2.5rem;
            font-weight: 400;
            letter-spacing: -2px;
        }

        .module-content .trend {
            font-size: 0.75rem;
            margin-top: 10px;
            color: var(--muted);
        }

        /* Large Canvas Module */
        .canvas-large {
            grid-column: 1 / -1;
            min-height: 450px;
            display: flex;
            flex-direction: column;
        }

        .placeholder-text {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            border: 1px dashed var(--border);
            margin-top: 1rem;
            color: var(--muted);
            font-size: 0.9rem;
            font-style: italic;
        }

        /* --- FOOTER --- */
        footer {
            margin-top: 8rem;
            padding: 3rem 0;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            font-size: 0.75rem;
            color: var(--muted);
            letter-spacing: 0.5px;
        }

        .footer-nav a {
            color: inherit;
            text-decoration: none;
            margin-left: 2rem;
            transition: color 0.3s;
        }

        .footer-nav a:hover { color: var(--black); }

        /* --- OVERLAY & MOBILE LOGIC --- */
        .overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(8px);
            z-index: 999;
        }

        @media (max-width: 1024px) {
            aside { left: -100%; width: 280px; }
            aside.is-open { left: 0; box-shadow: 50px 0 80px rgba(0,0,0,0.05); }
            main { margin-left: 0; padding: 2.5rem 5%; }
            .menu-trigger { display: block; }
            .overlay.is-active { display: block; }
        }

        @media (max-width: 600px) {
            header { flex-direction: column; align-items: flex-start; gap: 2rem; }
            footer { flex-direction: column; gap: 2rem; text-align: center; }
            .footer-nav a { margin: 0 1rem; }
        }
    </style>
</head>
<body>

    <div class="overlay" id="overlay"></div>

    <aside id="sidebar">
        <div class="brand-area">Sleek.v2</div>
        <nav class="nav-container">
            <a href="#" class="nav-link active">Dashboard</a>
            <a href="#" class="nav-item nav-link">Analytics</a>
            <a href="#" class="nav-item nav-link">Activity</a>
            <a href="#" class="nav-item nav-link">Settings</a>
        </nav>
    </aside>

    <main>
        <header>
            <div class="view-title">
                <h1>Interface Overview</h1>
                <p>Global system metrics and active workspaces.</p>
            </div>
            <button class="menu-trigger" id="menuBtn">Menu</button>
        </header>

        <section class="layout-grid">
            <div class="module">
                <span class="module-header">Network Performance</span>
                <div class="module-content">
                    <div class="value">99.9<small style="font-size: 1rem">%</small></div>
                    <div class="trend">Optimal Connection</div>
                </div>
            </div>

            <div class="module">
                <span class="module-header">Active Sessions</span>
                <div class="module-content">
                    <div class="value">1,402</div>
                    <div class="trend">+12% vs last hour</div>
                </div>
            </div>

            <div class="module">
                <span class="module-header">Avg. Response</span>
                <div class="module-content">
                    <div class="value">18<small style="font-size: 1rem">ms</small></div>
                    <div class="trend">Stable Latency</div>
                </div>
            </div>

            <div class="module canvas-large">
                <span class="module-header">Primary Workspace</span>
                <div class="placeholder-text">
                    Inject your primary application component (Tables, Charts, Editor) here.
                </div>
            </div>
        </section>

        <footer>
            <span>&copy; 2026 Sleek Architectural Systems</span>
            <div class="footer-nav">
                <a href="#">Support</a>
                <a href="#">Documentation</a>
                <a href="#">Privacy</a>
            </div>
        </footer>
    </main>

    <script>
        const menuBtn = document.getElementById('menuBtn');
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('overlay');

        // Toggle Function
        function toggleSidebar() {
            sidebar.classList.toggle('is-open');
            overlay.classList.toggle('is-active');
        }

        menuBtn.addEventListener('click', toggleSidebar);
        overlay.addEventListener('click', toggleSidebar);

        // Close on Link Click (Mobile)
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                // Remove active from all
                document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                // Add to clicked
                link.classList.add('active');
                
                if (window.innerWidth <= 1024) {
                    toggleSidebar();
                }
            });
        });
    </script>
</body>
</html>""",
    "Sleek Chat Room": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleek Chat | Minimalist Interface</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --border: #eeeeee;
            --black: #111111;
            --muted: #888888;
            --bubble-me: #111111;
            --bubble-them: #f1f1f1;
            --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--black);
            height: 100vh;
            display: flex;
            overflow: hidden;
        }

        /* --- SIDEBAR --- */
        aside {
            width: 320px;
            background: var(--surface);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }

        .sidebar-header {
            padding: 2.5rem 1.5rem;
            font-weight: 600;
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            border-bottom: 1px solid var(--border);
        }

        .chat-list {
            flex-grow: 1;
            overflow-y: auto;
        }

        .chat-item {
            padding: 1.5rem;
            border-bottom: 1px solid var(--border);
            cursor: pointer;
            transition: var(--transition);
        }

        .chat-item:hover { background: #fafafa; }
        .chat-item.active { background: #f5f5f5; border-right: 3px solid var(--black); }

        .chat-item h4 { font-size: 0.9rem; font-weight: 600; margin-bottom: 4px; }
        .chat-item p { font-size: 0.8rem; color: var(--muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

        /* --- CHAT MAIN WINDOW --- */
        main {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            background: var(--surface);
        }

        .chat-header {
            padding: 1.5rem 2rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chat-header h2 { font-size: 1rem; font-weight: 600; }

        #chat-window {
            flex-grow: 1;
            padding: 2rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
            scroll-behavior: smooth;
        }

        /* --- MESSAGE BUBBLES --- */
        .msg {
            max-width: 70%;
            padding: 1rem 1.25rem;
            font-size: 0.9rem;
            line-height: 1.5;
            position: relative;
            animation: slideIn 0.4s ease-out;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Sent by Me */
        .msg.me {
            align-self: flex-end;
            background: var(--bubble-me);
            color: white;
            border-radius: 18px 18px 0 18px;
        }

        /* Sent by Others */
        .msg.them {
            align-self: flex-start;
            background: var(--bubble-them);
            color: var(--black);
            border-radius: 18px 18px 18px 0;
        }

        .timestamp {
            font-size: 0.7rem;
            color: var(--muted);
            margin-top: 8px;
            display: block;
            text-align: right;
        }

        .them .timestamp { text-align: left; }

        /* --- INPUT AREA --- */
        .input-area {
            padding: 2rem;
            border-top: 1px solid var(--border);
            display: flex;
            gap: 1rem;
        }

        input {
            flex-grow: 1;
            padding: 1rem 1.5rem;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-family: inherit;
            font-size: 0.9rem;
            outline: none;
            transition: var(--transition);
        }

        input:focus { border-color: var(--black); }

        .send-btn {
            padding: 0 1.5rem;
            background: var(--black);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 500;
            font-size: 0.85rem;
            transition: var(--transition);
        }

        .send-btn:hover { opacity: 0.9; transform: translateY(-1px); }

        /* Hide Scrollbar */
        #chat-window::-webkit-scrollbar { width: 4px; }
        #chat-window::-webkit-scrollbar-track { background: transparent; }
        #chat-window::-webkit-scrollbar-thumb { background: #eee; }

        @media (max-width: 768px) {
            aside { display: none; }
        }
    </style>
</head>
<body>

    <aside>
        <div class="sidebar-header">Messages</div>
        <div class="chat-list">
            <div class="chat-item active">
                <h4>Design Team</h4>
                <p>The new dashboard look is sleek...</p>
            </div>
            <div class="chat-item">
                <h4>Alex Rivera</h4>
                <p>Did you check the latency stats?</p>
            </div>
        </div>
    </aside>

    <main>
        <div class="chat-header">
            <h2>Design Team</h2>
            <div style="color: var(--muted); font-size: 0.75rem;">3 Members Online</div>
        </div>

        <div id="chat-window">
            <div class="msg them">
                Hey! How is the new chat interface coming along?
                <span class="timestamp">10:45 AM</span>
            </div>
            <div class="msg me">
                Just finished the bubble design. It's clean.
                <span class="timestamp">10:46 AM</span>
            </div>
        </div>

        <form class="input-area" id="chat-form">
            <input type="text" id="chat-input" placeholder="Type a message..." autocomplete="off">
            <button type="submit" class="send-btn">Send</button>
        </form>
    </main>

    <script>
        const chatForm = document.getElementById('chat-form');
        const chatInput = document.getElementById('chat-input');
        const chatWindow = document.getElementById('chat-window');

        chatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const message = chatInput.value.trim();

            if (message) {
                renderMessage(message, 'me');
                chatInput.value = '';
                
                // Simulate a quick automated response for "cool aesthetic" feel
                setTimeout(() => {
                    renderMessage("System: Message delivered successfully.", 'them');
                }, 1000);
            }
        });

        function renderMessage(text, sender) {
            const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            
            const msgDiv = document.createElement('div');
            msgDiv.classList.add('msg', sender);
            
            msgDiv.innerHTML = `
                ${text}
                <span class="timestamp">${time}</span>
            `;

            chatWindow.appendChild(msgDiv);
            
            // Scroll to bottom
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
    </script>
</body>
</html>""",
    "Sleek Home Portal Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleek Portal | Minimalist Excellence</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #777777;
            --border: #eeeeee;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--black);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* --- NAVIGATION --- */
        nav {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 5%;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        /* Left: Logo + Name + Motto */
        .nav-left { display: flex; flex-direction: column; flex: 1; }
        .brand-name { font-weight: 700; font-size: 1.1rem; letter-spacing: 1px; line-height: 1.2; }
        .motto { font-size: 0.6rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; }

        /* Mid: Nav Links */
        .nav-mid { display: flex; gap: 2rem; flex: 2; justify-content: center; }
        .nav-mid a {
            text-decoration: none;
            color: var(--muted);
            font-size: 0.85rem;
            font-weight: 500;
            transition: var(--transition);
        }
        .nav-mid a:hover { color: var(--black); }

        /* Right: Profile + Extra */
        .nav-right { display: flex; align-items: center; justify-content: flex-end; gap: 1.5rem; flex: 1; }
        
        .profile-btn {
            width: 36px;
            height: 36px;
            background: var(--black);
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 0.7rem;
            transition: var(--transition);
        }
        .profile-btn:hover { transform: scale(1.05); }

        .extra-btn {
            padding: 8px 18px;
            border: 1px solid var(--black);
            font-size: 0.7rem;
            text-transform: uppercase;
            font-weight: 600;
            cursor: pointer;
            background: transparent;
            transition: var(--transition);
        }
        .extra-btn:hover { background: var(--black); color: white; }

        /* Mobile Toggle */
        .menu-toggle { display: none; cursor: pointer; font-size: 1.2rem; }

        /* --- HERO SECTION --- */
        .hero {
            padding: 8rem 5% 4rem;
            text-align: center;
            max-width: 1100px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: clamp(2.5rem, 8vw, 4.5rem);
            font-weight: 700;
            letter-spacing: -2px;
            line-height: 1.05;
            margin-bottom: 1.5rem;
        }

        .hero p {
            font-size: 1.1rem;
            color: var(--muted);
            margin-bottom: 3rem;
            max-width: 650px;
            margin-inline: auto;
        }

        .hero-btns { display: flex; justify-content: center; gap: 1rem; margin-bottom: 5rem; }

        .btn-prime { padding: 1.2rem 3rem; background: var(--black); color: white; border: none; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-ghost { padding: 1.2rem 3rem; border: 1px solid var(--border); background: transparent; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-prime:hover { opacity: 0.8; transform: translateY(-2px); }

        .hero-display {
            width: 100%;
            height: 550px;
            background: #f9f9f9;
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--muted);
            font-style: italic;
            border-radius: 4px;
        }

        /* --- BODY CARDS --- */
        .content-section { padding: 8rem 5%; background: #ffffff; }
        .section-title { font-size: 2.2rem; margin-bottom: 4rem; text-align: center; font-weight: 700; letter-spacing: -1px; }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
        }

        .card {
            padding: 4rem 2.5rem;
            background: white;
            border: 1px solid var(--border);
            transition: var(--transition);
        }

        .card:hover { border-color: var(--black); transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.02); }
        .card h3 { font-size: 1.3rem; margin-bottom: 1.2rem; font-weight: 600; }
        .card p { color: var(--muted); font-size: 0.95rem; margin-bottom: 2.5rem; line-height: 1.7; }
        .card button { background: transparent; border: none; font-weight: 700; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px; cursor: pointer; border-bottom: 1px solid transparent; transition: 0.3s; }
        .card button:hover { border-bottom: 1px solid var(--black); }

        /* --- FOOTER --- */
        footer {
            background: white;
            border-top: 1px solid var(--border);
            padding: 7rem 5% 3rem;
        }

        .footer-top {
            display: grid;
            grid-template-columns: 1.5fr 1fr 1fr;
            gap: 4rem;
            margin-bottom: 6rem;
        }

        .footer-section h4 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 2rem; color: var(--black); }
        .footer-section p, .footer-section a { font-size: 0.9rem; color: var(--muted); text-decoration: none; display: block; margin-bottom: 1rem; transition: 0.3s; }
        .footer-section a:hover { color: var(--black); }

        .footer-bottom {
            padding-top: 3rem;
            border-top: 1px solid var(--border);
            text-align: center;
            font-size: 0.7rem;
            color: var(--muted);
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        /* --- RESPONSIVE --- */
        @media (max-width: 1024px) {
            .nav-mid { display: none; }
            .menu-toggle { display: block; order: 2; margin-left: 1.5rem; }
            .nav-right { flex: initial; }
            .footer-top { grid-template-columns: 1fr; text-align: center; gap: 3rem; }
        }

        @media (max-width: 600px) {
            .hero { padding-top: 5rem; }
            .hero-btns { flex-direction: column; }
            .hero-display { height: 350px; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-left">
            <div class="brand-name">AESTHETE</div>
            <div class="motto">Refining the digital edge</div>
        </div>
        
        <div class="nav-mid" id="navLinks">
            <a href="#">Solutions</a>
            <a href="#">Architecture</a>
            <a href="#">Studio</a>
            <a href="#">About</a>
        </div>

        <div class="nav-right">
            <button class="extra-btn">Action</button>
            <div class="profile-btn">USR</div>
            <div class="menu-toggle" id="mobileMenu">☰</div>
        </div>
    </nav>

    <header class="hero">
        <h1>Building the future of minimalist design.</h1>
        <p>A sophisticated framework for developers who value clarity, performance, and high-end aesthetics above all else.</p>
        <div class="hero-btns">
            <button class="btn-prime">Get Started</button>
            <button class="btn-ghost">Documentation</button>
        </div>
        <div class="hero-display">
            [ Interactive Media or Product Showcase ]
        </div>
    </header>

    <section class="content-section">
        <h2 class="section-title">Core Philosophies</h2>
        <div class="card-grid">
            <div class="card">
                <h3>Semantic Structure</h3>
                <p>Clean code is the foundation of elegance. We prioritize HTML5 best practices for SEO and accessibility.</p>
                <button>Learn More &rarr;</button>
            </div>
            <div class="card">
                <h3>Visual Silence</h3>
                <p>Reducing noise allows the user to focus on what matters. Our layouts breathe with purposeful whitespace.</p>
                <button>Learn More &rarr;</button>
            </div>
            <div class="card">
                <h3>Adaptive Flow</h3>
                <p>From the smallest mobile screen to ultra-wide monitors, the design remains fluid and responsive.</p>
                <button>Learn More &rarr;</button>
            </div>
        </div>
    </section>

    <footer>
        <div class="footer-top">
            <div class="footer-section">
                <div class="brand-name">AESTHETE</div>
                <div class="motto" style="margin-bottom: 1.5rem;">The digital edge</div>
                <p>The pinnacle of modern web architecture. Crafting digital legacies through intent, precision, and architectural integrity.</p>
            </div>
            <div class="footer-section">
                <h4>Resources</h4>
                <a href="#">Know More</a>
                <a href="#">Support Center</a>
                <a href="#">FAQs</a>
                <a href="#">System Status</a>
            </div>
            <div class="footer-section">
                <h4>Connect</h4>
                <p>128 Studio Plaza, Lagos, NG</p>
                <p>+234 800 000 0000</p>
                <p>hello@aesthete.studio</p>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2026 AESTHETE STUDIO. ALL RIGHTS RESERVED.
        </div>
    </footer>

    <script>
        // Basic mobile menu toggle logic
        const mobileMenu = document.getElementById('mobileMenu');
        const navLinks = document.getElementById('navLinks');

        mobileMenu.addEventListener('click', () => {
            // In a real app, you'd toggle a mobile-specific overlay class here
            alert('Mobile navigation would slide in here, keeping the sleek aesthetic.');
        });
    </script>
</body>
</html>"""
,   "Sleek Admin Management Portal": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Management | Sleek OS</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--black); line-height: 1.5; }

        /* --- NAVIGATION --- */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 100;
        }
        .nav-left .brand { font-weight: 700; font-size: 1.1rem; letter-spacing: 1px; }
        .nav-left .motto { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; }
        .nav-right { display: flex; gap: 1.5rem; }
        .nav-btn { text-decoration: none; color: var(--muted); font-size: 0.85rem; font-weight: 500; transition: var(--transition); }
        .nav-btn:hover { color: var(--black); }

        /* --- GENERAL UTILITIES --- */
        section { padding: 4rem 5%; }
        .section-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2rem; }
        .title-block h2 { font-size: 1.5rem; font-weight: 600; letter-spacing: -0.5px; }
        .title-block p { font-size: 0.85rem; color: var(--muted); margin-top: 4px; }
        .btn-group { display: flex; gap: 0.75rem; }
        .btn-sm { padding: 0.5rem 1rem; border: 1px solid var(--border); background: white; font-size: 0.75rem; font-weight: 600; cursor: pointer; }
        .btn-sm:hover { border-color: var(--black); }

        /* --- SECTION 1: SCROLL LIST --- */
        .h-scroll {
            display: flex;
            gap: 1.5rem;
            overflow-x: auto;
            padding-bottom: 1rem;
            scrollbar-width: none;
        }
        .h-scroll::-webkit-scrollbar { display: none; }
        .stat-card {
            min-width: 280px;
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 1.5rem;
        }
        .card-icons { display: flex; justify-content: space-between; margin-bottom: 2rem; color: var(--muted); }
        .stat-card .count { font-size: 2rem; font-weight: 400; }
        .stat-card .desc { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }

        /* --- SECTION 2 & 3: DUAL CARDS & TABLES --- */
        .dual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 3rem; }
        .card-info { background: var(--surface); border: 1px solid var(--border); padding: 2rem; }
        .card-info h3 { font-size: 0.8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
        .card-info .big-num { font-size: 2.5rem; margin: 1rem 0; font-weight: 500; }
        .card-info .sub-desc { font-size: 0.85rem; color: var(--muted); }

        .sub-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        .table-wrap { background: var(--surface); border: 1px solid var(--border); margin-top: 1rem; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 1rem; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; background: #fafafa; border-bottom: 1px solid var(--border); }
        td { padding: 1rem; border-bottom: 1px solid var(--border); font-size: 0.85rem; }
        tr:last-child td { border-bottom: none; }

        /* --- LIST ITEMS (Section 3) --- */
        .list-wrap { border-top: 1px solid var(--border); margin-top: 1rem; }
        .list-item { display: flex; justify-content: space-between; padding: 1rem 0; border-bottom: 1px solid var(--border); }
        .list-item .meta h5 { font-size: 0.9rem; font-weight: 600; }
        .list-item .meta span { font-size: 0.75rem; color: var(--muted); }
        .list-item .time { font-size: 0.75rem; color: var(--muted); font-family: monospace; }

        /* --- SECTION 4: PROGRESS & SMALL CARDS --- */
        .four-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; }
        
        .progress-list { margin-top: 2rem; }
        .progress-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem; font-size: 0.8rem; }
        .label-month { width: 50px; color: var(--muted); }
        .bar-bg { flex-grow: 1; height: 8px; background: var(--border); border-radius: 10px; position: relative; }
        .bar-fill { height: 100%; background: var(--black); border-radius: 10px; }
        .perc-text { width: 40px; text-align: right; font-weight: 600; }

        .trio-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 3rem; }
        .mini-list { margin-top: 1rem; }
        .mini-item { display: flex; justify-content: space-between; font-size: 0.85rem; padding: 0.5rem 0; border-bottom: 1px dashed var(--border); }

        /* --- FOOTER --- */
        footer { padding: 5rem 5% 2rem; border-top: 1px solid var(--border); background: white; margin-top: 4rem; }
        .f-top { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 4rem; margin-bottom: 4rem; }
        .f-section h4 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem; }
        .f-section p, .f-section a { font-size: 0.85rem; color: var(--muted); text-decoration: none; display: block; margin-bottom: 0.75rem; }
        .f-bottom { padding-top: 2rem; border-top: 1px solid var(--border); text-align: center; font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 2px; }

        @media (max-width: 1024px) {
            .dual-grid, .sub-grid, .four-grid, .trio-grid { grid-template-columns: 1fr; }
            .f-top { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-left">
            <div class="brand">CORE ADMIN</div>
            <div class="motto">System Architecture v1.0</div>
        </div>
        <div class="nav-right">
            <a href="#" class="nav-btn">Terminal</a>
            <a href="#" class="nav-btn">Users</a>
            <a href="#" class="nav-btn">Settings</a>
        </div>
    </nav>

    <section>
        <div class="section-header">
            <div class="title-block">
                <h2>System Health</h2>
                <p>Real-time monitor of core hardware clusters.</p>
            </div>
        </div>
        <div class="h-scroll">
            <div class="stat-card">
                <div class="card-icons"><span>⬢</span><span>⚙</span></div>
                <div class="count">89.4%</div>
                <div class="desc">Cpu Efficiency</div>
            </div>
            <div class="stat-card">
                <div class="card-icons"><span>⬡</span><span>⚙</span></div>
                <div class="count">12.1ms</div>
                <div class="desc">Avg Latency</div>
            </div>
            <div class="stat-card">
                <div class="card-icons"><span>✦</span><span>⚙</span></div>
                <div class="count">1,024</div>
                <div class="desc">Active Nodes</div>
            </div>
            <div class="stat-card">
                <div class="card-icons"><span>◈</span><span>⚙</span></div>
                <div class="count">02</div>
                <div class="desc">Incidents</div>
            </div>
        </div>
    </section>

    <section>
        <div class="section-header">
            <div class="title-block">
                <h2>Traffic Intelligence</h2>
            </div>
            <div class="btn-group">
                <button class="btn-sm">Export</button>
                <button class="btn-sm">Filter</button>
            </div>
        </div>
        <div class="dual-grid">
            <div class="card-info">
                <h3>Global Reach</h3>
                <div class="big-num">142</div>
                <div class="sub-desc">Active entry points across 12 regions.</div>
            </div>
            <div class="card-info">
                <h3>Unique Visitors</h3>
                <div class="big-num">8.4k</div>
                <div class="sub-desc">Verified unique sessions in 24h.</div>
            </div>
        </div>
        <div class="sub-grid">
            <div class="sub-col">
                <div class="title-block"><h2>Entry Logs</h2></div>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Location</th><th>IP Address</th><th>Time</th></tr></thead>
                        <tbody>
                            <tr><td>Lagos, NG</td><td>192.168.1.1</td><td>12:04:01</td></tr>
                            <tr><td>London, UK</td><td>104.22.1.84</td><td>12:02:55</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="sub-col">
                <div class="title-block"><h2>Exit Logs</h2></div>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Node</th><th>Duration</th><th>Status</th></tr></thead>
                        <tbody>
                            <tr><td>Node-A</td><td>45m</td><td>Closed</td></tr>
                            <tr><td>Node-Z</td><td>12h</td><td>Timeout</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="section-header">
            <div class="title-block"><h2>User Infrastructure</h2></div>
            <div class="btn-group">
                <button class="btn-sm">Manage</button>
                <button class="btn-sm">Refresh</button>
            </div>
        </div>
        <div class="dual-grid">
            <div class="card-info">
                <h3>New Accounts</h3>
                <div class="big-num">422</div>
                <div class="sub-desc">Growth rate +12% this week.</div>
            </div>
            <div class="card-info">
                <h3>Active Licenses</h3>
                <div class="big-num">2.1k</div>
                <div class="sub-desc">Enterprise level verification.</div>
            </div>
        </div>
        <div class="sub-grid">
            <div class="sub-col">
                <div class="title-block"><h2>Team Leads</h2></div>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Name</th><th>Role</th></tr></thead>
                        <tbody>
                            <tr><td>Alex Rivera</td><td>Lead Arch</td></tr>
                            <tr><td>Sarah Chen</td><td>Sec Ops</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="sub-col">
                <div class="title-block"><h2>Staff Access</h2></div>
                <div class="table-wrap">
                    <table>
                        <thead><tr><th>Dept</th><th>Clearance</th></tr></thead>
                        <tbody>
                            <tr><td>DevOps</td><td>Level 4</td></tr>
                            <tr><td>Legal</td><td>Level 2</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div style="margin-top: 3rem;">
            <div class="title-block"><h2>Activity Stream</h2></div>
            <div class="list-wrap">
                <div class="list-item">
                    <div class="meta"><h5>System Update</h5><span>Kernel patch applied across clusters.</span></div>
                    <div class="time">14:22:01</div>
                </div>
                <div class="list-item">
                    <div class="meta"><h5>Database Backup</h5><span>Automated snapshot completed.</span></div>
                    <div class="time">12:00:00</div>
                </div>
            </div>
        </div>
    </section>

    <section>
        <div class="section-header">
            <div class="title-block">
                <h2>Performance Matrix</h2>
                <p>Quarterly efficiency and resource allocation.</p>
            </div>
        </div>
        <div class="four-grid">
            <div class="card-info" style="padding: 1.5rem">
                <h3>Storage</h3><div class="big-num" style="font-size: 1.5rem">4.2 TB</div><div class="sub-desc">84% Capacity</div>
            </div>
            <div class="card-info" style="padding: 1.5rem">
                <h3>Bandwidth</h3><div class="big-num" style="font-size: 1.5rem">1.2 Gbps</div><div class="sub-desc">Peak Usage</div>
            </div>
            <div class="card-info" style="padding: 1.5rem">
                <h3>Uptime</h3><div class="big-num" style="font-size: 1.5rem">99.98%</div><div class="sub-desc">Last 30 Days</div>
            </div>
            <div class="card-info" style="padding: 1.5rem">
                <h3>Errors</h3><div class="big-num" style="font-size: 1.5rem">14</div><div class="sub-desc">Resolved</div>
            </div>
        </div>

        <div class="progress-list" style="max-width: 600px;">
            <div class="section-header" style="margin-bottom: 1rem;">
                <div class="title-block"><h2>Resource Cycle</h2><p>Monthly allocation</p></div>
                <div class="perc-text" style="width: auto">Avg 78%</div>
            </div>
            <div class="progress-row"><div class="label-month">JAN</div><div class="bar-bg"><div class="bar-fill" style="width: 80%"></div></div><div class="perc-text">80%</div></div>
            <div class="progress-row"><div class="label-month">FEB</div><div class="bar-bg"><div class="bar-fill" style="width: 65%"></div></div><div class="perc-text">65%</div></div>
        </div>

        <div class="trio-grid">
            <div class="module-mini">
                <div class="title-block"><h3>Regional Load</h3></div>
                <div class="mini-list">
                    <div class="mini-item"><span>US-East</span><strong>42%</strong></div>
                    <div class="mini-item"><span>EU-West</span><strong>31%</strong></div>
                </div>
            </div>
            <div class="module-mini">
                <div class="title-block"><h3>Asset Health</h3></div>
                <div class="mini-list">
                    <div class="mini-item"><span>Servers</span><strong>Healthy</strong></div>
                    <div class="mini-item"><span>CDNs</span><strong>Stable</strong></div>
                </div>
            </div>
            <div class="module-mini">
                <div class="title-block"><h3>Auth Logs</h3></div>
                <div class="mini-list">
                    <div class="mini-item"><span>Successful</span><strong>14.2k</strong></div>
                    <div class="mini-item"><span>Blocked</span><strong>102</strong></div>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="f-top">
            <div class="f-section">
                <div class="brand">CORE ADMIN</div>
                <p style="margin-top:1rem">A secure, minimalist architecture for system management and infrastructure control.</p>
            </div>
            <div class="f-section">
                <h4>Resources</h4>
                <a href="#">Github Repository</a>
                <a href="#">API Documentation</a>
                <a href="#">Support Ticket</a>
                <a href="#">FAQs</a>
            </div>
            <div class="f-section">
                <h4>System Status</h4>
                <p>● All Systems Operational</p>
                <p>Last Updated: 12:00:00</p>
                <p>Server Time: UTC +0</p>
            </div>
        </div>
        <div class="f-bottom">
            &copy; 2026 CORE ADMIN STUDIO. ALL RIGHTS RESERVED.
        </div>
    </footer>

</body>
</html>""",
    "Sleek Principal Management Portal": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Principal Overseer | Management Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --input-bg: #f9f9f9;
            --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--black); line-height: 1.5; }

        /* --- NAVIGATION --- */
        nav {
            display: flex; justify-content: space-between; align-items: center;
            padding: 1.5rem 5%; background: var(--surface); border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 1000;
        }
        .nav-left .brand { font-weight: 700; font-size: 1.1rem; letter-spacing: 1px; }
        .nav-left .motto { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; }
        .nav-right { display: flex; gap: 1.5rem; }
        .nav-link { text-decoration: none; color: var(--muted); font-size: 0.85rem; font-weight: 500; transition: var(--transition); }
        .nav-link:hover { color: var(--black); }

        /* --- LAYOUT UTILITIES --- */
        section { padding: 4rem 5%; }
        .header-block { margin-bottom: 2.5rem; display: flex; justify-content: space-between; align-items: flex-end; }
        .title-group h2 { font-size: 1.6rem; font-weight: 600; letter-spacing: -0.5px; }
        .title-group p { font-size: 0.85rem; color: var(--muted); margin-top: 4px; }
        .header-meta { display: flex; gap: 1.5rem; align-items: center; }
        .meta-item { display: flex; align-items: center; gap: 6px; font-size: 0.75rem; color: var(--muted); font-weight: 500; }

        /* --- SECTION 1: HORIZONTAL SCROLL --- */
        .h-scroll { display: flex; gap: 1.5rem; overflow-x: auto; padding-bottom: 1rem; scrollbar-width: none; }
        .h-scroll::-webkit-scrollbar { display: none; }
        .scroll-card { min-width: 300px; background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; transition: var(--transition); }
        .scroll-card:hover { border-color: var(--black); }
        .card-head { display: flex; justify-content: space-between; margin-bottom: 2rem; color: var(--muted); }
        .scroll-card .count { font-size: 2.2rem; font-weight: 400; }
        .scroll-card .label { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }

        /* --- SECTION 2: QUAD GRID & SUBSECTIONS --- */
        .quad-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-bottom: 4rem; }
        .overseer-card { background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; }
        .card-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
        .tag { font-size: 0.6rem; padding: 2px 8px; border: 1px solid var(--border); text-transform: uppercase; }
        .overseer-card h4 { font-size: 0.85rem; color: var(--muted); font-weight: 500; }
        .overseer-card .mid-num { font-size: 1.8rem; margin: 0.8rem 0; font-weight: 600; }
        .overseer-card .desc-line { font-size: 0.75rem; color: var(--muted); display: block; }

        .subsection { margin-top: 5rem; }
        
        /* Tables */
        .input-table-wrap { margin-top: 1.5rem; }
        .input-table { width: 100%; border-collapse: collapse; }
        .input-table th { text-align: left; padding: 1rem; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1.5px; color: var(--muted); }
        .input-table td { padding: 0.5rem 1rem; }
        .ui-input { width: 100%; padding: 0.8rem; border: 1px solid var(--border); background: var(--input-bg); font-family: inherit; font-size: 0.85rem; outline: none; }
        .ui-input:focus { border-color: var(--black); background: #fff; }

        .vertical-table-wrap { margin-top: 1.5rem; border-top: 1px solid var(--border); }
        .v-table { width: 100%; border-collapse: collapse; }
        .v-table th { padding: 1.2rem 1rem; text-align: left; border-bottom: 1px solid var(--border); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; background: #fafafa; }
        .v-table td { padding: 1.2rem 1rem; border-bottom: 1px solid var(--border); font-size: 0.85rem; }
        .table-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; }

        /* Visualization Frames */
        .viz-frame { width: 100%; height: 400px; background: #f0f0f0; border: 1px dashed var(--border); display: flex; align-items: center; justify-content: center; margin-top: 1.5rem; color: var(--muted); font-size: 0.85rem; font-style: italic; }

        /* Buttons */
        .btn-set { display: flex; gap: 1rem; margin-top: 1.5rem; }
        .btn-black { padding: 0.8rem 1.5rem; background: var(--black); color: white; border: none; font-size: 0.75rem; font-weight: 600; cursor: pointer; }
        .btn-outline { padding: 0.8rem 1.5rem; border: 1px solid var(--border); background: white; font-size: 0.75rem; font-weight: 600; cursor: pointer; }

        /* Sub 4 Grid */
        .mini-quad { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 1.5rem; }
        .mini-card { padding: 1.2rem; border: 1px solid var(--border); background: #fff; }
        .mini-card span { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
        .mini-card div { font-size: 1.2rem; font-weight: 600; margin-top: 4px; }

        /* --- FOOTER --- */
        footer { padding: 6rem 5% 3rem; border-top: 1px solid var(--border); background: white; margin-top: 4rem; }
        .f-container { display: grid; grid-template-columns: 1.5fr 1fr 1fr; gap: 4rem; margin-bottom: 4rem; }
        .f-col h4 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem; }
        .f-col p, .f-col a { font-size: 0.85rem; color: var(--muted); text-decoration: none; display: block; margin-bottom: 0.8rem; }
        .f-copy { padding-top: 3rem; border-top: 1px solid var(--border); text-align: center; font-size: 0.7rem; color: var(--muted); letter-spacing: 2px; }

        @media (max-width: 1024px) {
            .f-container, .quad-grid, .mini-quad { grid-template-columns: 1fr; }
            .header-block { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-left">
            <div class="brand">PRINCIPAL OVERSEER</div>
            <div class="motto">Directorial Control & Governance</div>
        </div>
        <div class="nav-right">
            <a href="#" class="nav-link">Strategy</a>
            <a href="#" class="nav-link">Governance</a>
            <a href="#" class="nav-link">Resources</a>
        </div>
    </nav>

    <section>
        <div class="header-block">
            <div class="title-group">
                <h2>Operational Pulse</h2>
                <p>High-level performance indicators across all sectors.</p>
            </div>
        </div>
        <div class="h-scroll">
            <div class="scroll-card">
                <div class="card-head"><span>⌘</span><span>⊕</span></div>
                <div class="count">94.2%</div>
                <div class="label">Compliance Rating</div>
            </div>
            <div class="scroll-card">
                <div class="card-head"><span>⌬</span><span>⊖</span></div>
                <div class="count">1.4s</div>
                <div class="label">Decision Latency</div>
            </div>
            <div class="scroll-card">
                <div class="card-head"><span>⏀</span><span>⊛</span></div>
                <div class="count">24k</div>
                <div class="label">Asset Volume</div>
            </div>
            <div class="scroll-card">
                <div class="card-head"><span>⋈</span><span>⊗</span></div>
                <div class="count">08</div>
                <div class="label">Critical Warnings</div>
            </div>
        </div>
    </section>

    <section>
        <div class="header-block">
            <div class="title-group">
                <h2>Governance Framework</h2>
                <p>Strategic oversight and systemic adjustments.</p>
            </div>
        </div>

        <div class="quad-grid">
            <div class="overseer-card">
                <div class="card-top"><span>◈</span><span class="tag">Active</span></div>
                <h4>Personnel Flow</h4>
                <div class="mid-num">1,840</div>
                <span class="desc-line">Inbound: 42 today</span>
                <span class="desc-line">Outbound: 12 today</span>
            </div>
            <div class="overseer-card">
                <div class="card-top"><span>⬢</span><span class="tag">Stable</span></div>
                <h4>Resource Cap</h4>
                <div class="mid-num">$4.2M</div>
                <span class="desc-line">Allocated: 82%</span>
                <span class="desc-line">Reserve: 18%</span>
            </div>
            <div class="overseer-card">
                <div class="card-top"><span>⧉</span><span class="tag">Review</span></div>
                <h4>Policy Compliance</h4>
                <div class="mid-num">98.1%</div>
                <span class="desc-line">Internal Audit Pending</span>
                <span class="desc-line">Last Check: 2h ago</span>
            </div>
            <div class="overseer-card">
                <div class="card-top"><span>⩇</span><span class="tag">Alert</span></div>
                <h4>System Stress</h4>
                <div class="mid-num">14%</div>
                <span class="desc-line">Load: Normal</span>
                <span class="desc-line">Thermal: Optimal</span>
            </div>
        </div>

        <div class="subsection">
            <div class="title-group">
                <h2>Policy Adjustment</h2>
                <p>Modify systemic parameters in real-time.</p>
            </div>
            <div class="input-table-wrap">
                <table class="input-table">
                    <thead>
                        <tr>
                            <th>Parameter Name</th>
                            <th>Target Value</th>
                            <th>Priority Level</th>
                            <th>Adjustment Filter</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><input type="text" class="ui-input" placeholder="e.g. Bandwidth"></td>
                            <td><input type="text" class="ui-input" placeholder="0.00"></td>
                            <td><input type="text" class="ui-input" placeholder="High/Low"></td>
                            <td>
                                <select class="ui-input">
                                    <option>Global</option>
                                    <option>Regional</option>
                                </select>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="btn-set">
                    <button class="btn-black">Apply Changes</button>
                    <button class="btn-outline">Reset</button>
                </div>
            </div>
        </div>

        <div class="subsection">
            <div class="header-block">
                <div class="title-group">
                    <h2>Structural Mapping</h2>
                    <p>Hierarchical visualization of organizational nodes.</p>
                </div>
                <div class="header-meta">
                    <div class="meta-item"><span>▣</span> Node View</div>
                    <div class="meta-item"><span>◚</span> Flow Map</div>
                    <div class="meta-item"><span>◛</span> Heatmap</div>
                </div>
            </div>
            <div class="viz-frame">[ System Node Topology Visualization ]</div>
        </div>

        <div class="subsection">
            <div class="title-group">
                <h2>Detailed Audit Log</h2>
                <p>Chronological record of recent governance actions.</p>
            </div>
            <div class="vertical-table-wrap">
                <table class="v-table">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Overseer ID</th>
                            <th>Action Taken</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td>2026.02.27</td><td>PO-842</td><td>Resource Reallocation</td><td>Verified</td></tr>
                        <tr><td>2026.02.26</td><td>PO-119</td><td>Policy Update v2.4</td><td>Active</td></tr>
                        <tr><td>2026.02.26</td><td>SYS-00</td><td>Automated Scrub</td><td>Complete</td></tr>
                    </tbody>
                </table>
                <div class="table-footer">
                    <p style="font-size: 0.75rem; color: var(--muted)">Showing 3 of 142 entries in the current cycle.</p>
                    <div class="btn-set" style="margin-top: 0">
                        <button class="btn-outline">Previous</button>
                        <button class="btn-outline">Next</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="subsection">
            <div class="header-block">
                <div class="title-group">
                    <h2>Trend Analysis</h2>
                    <p>Forecasting and historical data comparisons.</p>
                </div>
                <div class="header-meta">
                    <div class="meta-item"><span>⏍</span> Data A</div>
                    <div class="meta-item"><span>⏏</span> Data B</div>
                    <div class="meta-item"><span>⏚</span> Data C</div>
                    <div class="meta-item"><span>⏛</span> Data D</div>
                </div>
            </div>
            <div class="viz-frame" style="height: 300px;">[ Historical Trend Line Chart ]</div>
            <div class="mini-quad">
                <div class="mini-card"><span>Baseline</span><div>1,042</div></div>
                <div class="mini-card"><span>Current</span><div>1,284</div></div>
                <div class="mini-card"><span>Delta</span><div>+242</div></div>
                <div class="mini-card"><span>Projection</span><div>1,400</div></div>
            </div>
        </div>
    </section>

    <footer>
        <div class="f-container">
            <div class="f-col">
                <div class="brand">PRINCIPAL OVERSEER</div>
                <p style="margin-top: 1rem;">Architecting the standards of digital governance and operational excellence in 2026.</p>
            </div>
            <div class="f-col">
                <h4>Resources</h4>
                <a href="#">Know More</a>
                <a href="#">Support Center</a>
                <a href="#">FAQs</a>
                <a href="#">Security Protocols</a>
            </div>
            <div class="f-col">
                <h4>Contact</h4>
                <p>128 Central Axis, Tech District</p>
                <p>+1 (800) OVERSEER</p>
                <p>admin@overseer.studio</p>
            </div>
        </div>
        <div class="f-copy">
            &copy; 2026 PRINCIPAL OVERSEER PLATFORM. ALL RIGHTS RESERVED.
        </div>
    </footer>

</body>
</html>""",
    "Sleek Sign Up Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up | Sleek OS</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --input-bg: #f9f9f9;
            --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--black); height: 100vh; overflow: hidden; }

        .split-container { display: flex; height: 100vh; width: 100%; }

        /* LEFT PANEL */
        .panel-left {
            flex: 1;
            background: var(--black);
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 4rem;
        }

        .logo-circle {
            width: 70px; height: 70px; border: 2px solid white; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; margin-bottom: 1.5rem;
        }

        .panel-left h1 { font-size: 1.5rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 1rem; }
        .panel-left p { font-size: 0.85rem; color: #aaaaaa; max-width: 280px; line-height: 1.6; }

        /* RIGHT PANEL - FIXED VERTICAL ALIGNMENT */
        .panel-right {
            flex: 1;
            background: var(--surface);
            display: flex;
            flex-direction: column;
            padding: 3rem 10%;
        }

        /* This container grows to push the footer down */
        .form-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center; /* Centers the form in the available space */
        }

        .form-header { margin-bottom: 2rem; }
        .form-header h2 { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .form-header p { color: var(--muted); font-size: 0.9rem; }

        .input-group { margin-bottom: 1.2rem; }
        .input-group label { display: block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
        
        .field-wrapper { position: relative; display: flex; align-items: center; }
        
        .ui-input {
            width: 100%; padding: 0.9rem; border: 1px solid var(--border);
            background: var(--input-bg); font-family: inherit; font-size: 0.9rem; outline: none;
        }

        .ui-input:focus { border-color: var(--black); background: white; }

        .toggle-pass {
            position: absolute; right: 1rem; font-size: 0.65rem;
            font-weight: 700; text-transform: uppercase; cursor: pointer; color: var(--muted);
        }

        .input-desc { font-size: 0.65rem; color: var(--muted); margin-top: 5px; }

        .btn-main {
            width: 100%; padding: 1rem; background: var(--black); color: white;
            border: none; font-size: 0.8rem; font-weight: 600; text-transform: uppercase;
            letter-spacing: 1px; cursor: pointer; margin-top: 1rem;
        }

        .btn-google {
            width: 100%; padding: 0.9rem; background: transparent; border: 1px solid var(--border);
            font-size: 0.8rem; cursor: pointer; margin-top: 0.8rem;
            display: flex; align-items: center; justify-content: center; gap: 8px;
        }

        .form-nav { text-align: center; margin-top: 1.5rem; font-size: 0.8rem; color: var(--muted); }
        .form-nav a { color: var(--black); text-decoration: none; font-weight: 700; }

        /* FOOTER AT THE BOTTOM */
        .panel-footer {
            padding-top: 2rem;
            font-size: 0.75rem;
            color: var(--muted);
            text-align: center;
            border-top: 1px solid #f5f5f5;
        }

        @media (max-width: 900px) {
            .panel-left { display: none; }
            .panel-right { padding: 2rem 8%; }
        }
    </style>
</head>
<body>

    <div class="split-container">
        <div class="panel-left">
            <div class="logo-circle">S</div>
            <h1>SLEEK OS</h1>
            <p>The definitive standard in architectural digital governance.</p>
        </div>

        <div class="panel-right">
            <div class="form-content">
                <div class="form-header">
                    <h2>Create an account</h2>
                    <p>Join the next generation of systemic overseers.</p>
                </div>

                <form>
                    <div class="input-group">
                        <label>Full Name</label>
                        <input type="text" class="ui-input" placeholder="Alexander Rivera">
                    </div>

                    <div class="input-group">
                        <label>Email Address</label>
                        <input type="email" class="ui-input" placeholder="admin@sleekos.com">
                    </div>

                    <div class="input-group">
                        <label>Password</label>
                        <div class="field-wrapper">
                            <input type="password" class="ui-input" placeholder="••••••••">
                            <span class="toggle-pass">See</span>
                        </div>
                        <p class="input-desc">Must contain 8+ characters with uppercase and symbols.</p>
                    </div>

                    <button type="submit" class="btn-main">Create Account</button>
                    <button type="button" class="btn-google">
                        <img src="https://www.google.com/favicon.ico" width="14" alt="G">
                        Sign up with Google
                    </button>
                </form>

                <p class="form-nav">Already have an account? <a href="#">Sign In</a></p>
            </div>

            <div class="panel-footer">
                Need support? Contact <span style="color: var(--black); font-weight: 500;">systems@sleekos.io</span>
            </div>
        </div>
    </div>

</body>
</html>""",
    "Sleek Sign In Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign In | Sleek OS</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --input-bg: #f9f9f9;
            --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--black); height: 100vh; overflow: hidden; }

        .split-container { display: flex; height: 100vh; width: 100%; }

        /* LEFT PANEL */
        .panel-left {
            flex: 1;
            background: var(--black);
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 4rem;
        }

        .logo-circle {
            width: 70px; height: 70px; border: 2px solid white; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; margin-bottom: 1.5rem;
        }

        .panel-left h1 { font-size: 1.5rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 1rem; }
        .panel-left p { font-size: 0.85rem; color: #aaaaaa; max-width: 280px; line-height: 1.6; }

        /* RIGHT PANEL - FIXED VERTICAL ALIGNMENT */
        .panel-right {
            flex: 1;
            background: var(--surface);
            display: flex;
            flex-direction: column;
            padding: 3rem 10%;
        }

        /* This container grows to push the footer down */
        .form-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center; /* Centers the form in the available space */
        }

        .form-header { margin-bottom: 2rem; }
        .form-header h2 { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .form-header p { color: var(--muted); font-size: 0.9rem; }

        .input-group { margin-bottom: 1.2rem; }
        .input-group label { display: block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px; }
        
        .field-wrapper { position: relative; display: flex; align-items: center; }
        
        .ui-input {
            width: 100%; padding: 0.9rem; border: 1px solid var(--border);
            background: var(--input-bg); font-family: inherit; font-size: 0.9rem; outline: none;
        }

        .ui-input:focus { border-color: var(--black); background: white; }

        .toggle-pass {
            position: absolute; right: 1rem; font-size: 0.65rem;
            font-weight: 700; text-transform: uppercase; cursor: pointer; color: var(--muted);
        }

        .input-desc { font-size: 0.65rem; color: var(--muted); margin-top: 5px; }

        .btn-main {
            width: 100%; padding: 1rem; background: var(--black); color: white;
            border: none; font-size: 0.8rem; font-weight: 600; text-transform: uppercase;
            letter-spacing: 1px; cursor: pointer; margin-top: 1rem;
        }

        .btn-google {
            width: 100%; padding: 0.9rem; background: transparent; border: 1px solid var(--border);
            font-size: 0.8rem; cursor: pointer; margin-top: 0.8rem;
            display: flex; align-items: center; justify-content: center; gap: 8px;
        }

        .form-nav { text-align: center; margin-top: 1.5rem; font-size: 0.8rem; color: var(--muted); }
        .form-nav a { color: var(--black); text-decoration: none; font-weight: 700; }

        /* FOOTER AT THE BOTTOM */
        .panel-footer {
            padding-top: 2rem;
            font-size: 0.75rem;
            color: var(--muted);
            text-align: center;
            border-top: 1px solid #f5f5f5;
        }

        @media (max-width: 900px) {
            .panel-left { display: none; }
            .panel-right { padding: 2rem 8%; }
        }
    </style>
</head>
<body>

    <div class="split-container">
        <div class="panel-left">
            <div class="logo-circle">S</div>
            <h1>SLEEK OS</h1>
            <p>The definitive standard in architectural digital governance.</p>
        </div>

        <div class="panel-right">
            <div class="form-content">
                <div class="form-header">
                    <h2>Welcome back</h2>
                    <p>Authorized access only. Please verify your identity.</p>
                </div>

                <form>
                    <div class="input-group">
                        <label>Email Address</label>
                        <input type="email" class="ui-input" placeholder="admin@sleekos.com">
                    </div>

                    <div class="input-group">
                        <label>Password</label>
                        <div class="field-wrapper">
                            <input type="password" class="ui-input" placeholder="••••••••">
                            <span class="toggle-pass">See</span>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                        <label style="display: flex; align-items: center; gap: 6px; font-size: 0.75rem; cursor: pointer;">
                            <input type="checkbox" style="accent-color: black;"> Remember me
                        </label>
                        <a href="#" style="font-size: 0.75rem; color: var(--muted); text-decoration: none;">Forgot Password?</a>
                    </div>

                    <button type="submit" class="btn-main">Sign In</button>
                    <button type="button" class="btn-google">
                        <img src="https://www.google.com/favicon.ico" width="14" alt="G">
                        Sign in with Google
                    </button>
                </form>

                <p class="form-nav">New to the system? <a href="#">Create Account</a></p>
            </div>

            <div class="panel-footer">
                Need support? Contact <span style="color: var(--black); font-weight: 500;">systems@sleekos.io</span>
            </div>
        </div>
    </div>

</body>
</html>""",
    "Sleek About Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | Sleek OS</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Inter', sans-serif; 
            background: var(--bg); 
            color: var(--black); 
            line-height: 1.6;
        }

        /* --- NAVIGATION --- */
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 5%;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .nav-left .brand { font-weight: 700; font-size: 1.1rem; letter-spacing: 1px; line-height: 1.2; }
        .nav-left .motto { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; }
        .nav-right { display: flex; gap: 2rem; }
        .nav-link { text-decoration: none; color: var(--muted); font-size: 0.85rem; font-weight: 500; transition: var(--transition); }
        .nav-link:hover { color: var(--black); }

        /* --- HERO / HEADER --- */
        .hero {
            padding: 8rem 5% 4rem;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .hero h1 {
            font-size: clamp(2.5rem, 8vw, 4.5rem);
            font-weight: 700;
            letter-spacing: -2px;
            line-height: 1.1;
            margin-bottom: 1.5rem;
        }
        .hero p {
            font-size: 1.15rem;
            color: var(--muted);
            margin-bottom: 2.5rem;
            max-width: 600px;
        }
        .hero-btns { display: flex; gap: 1rem; }
        .btn-black { padding: 1rem 2.5rem; background: var(--black); color: white; border: none; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-outline { padding: 1rem 2.5rem; border: 1px solid var(--border); background: transparent; font-size: 0.85rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-black:hover { opacity: 0.8; transform: translateY(-2px); }

        /* --- BODY SECTIONS --- */
        .content-section {
            padding: 6rem 5%;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .section-header { margin-bottom: 4rem; max-width: 700px; }
        .section-header h2 { font-size: 2rem; font-weight: 700; letter-spacing: -1px; margin-bottom: 0.5rem; }
        .section-header p { color: var(--muted); font-size: 1rem; }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            width: 100%;
        }
        .info-card {
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 3rem 2rem;
            transition: var(--transition);
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .info-card:hover { border-color: var(--black); transform: translateY(-5px); }
        .card-icon { font-size: 2rem; margin-bottom: 1.5rem; color: var(--black); }
        .card-mid { font-size: 1.25rem; font-weight: 600; margin-bottom: 1rem; letter-spacing: -0.5px; }
        .card-desc { font-size: 0.9rem; color: var(--muted); line-height: 1.7; }

        /* --- FOOTER --- */
        footer {
            margin-top: 6rem;
            padding: 6rem 5% 2rem;
            background: var(--surface);
            border-top: 1px solid var(--border);
        }
        .f-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 4rem;
            margin-bottom: 4rem;
        }
        .f-col .brand { font-weight: 700; font-size: 1rem; letter-spacing: 1px; margin-bottom: 0.5rem; }
        .f-col h4 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem; }
        .f-col p, .f-col a { font-size: 0.85rem; color: var(--muted); text-decoration: none; display: block; margin-bottom: 0.8rem; }
        .f-col a:hover { color: var(--black); }

        .f-bottom {
            padding-top: 2rem;
            border-top: 1px solid var(--border);
            text-align: center;
            font-size: 0.75rem;
            color: var(--muted);
            letter-spacing: 1px;
        }

        /* --- RESPONSIVE --- */
        @media (max-width: 1024px) {
            .card-grid, .f-container { grid-template-columns: 1fr; }
            .hero h1 { font-size: 3rem; }
            .f-container { text-align: center; gap: 3rem; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-left">
            <div class="brand">SLEEK OS</div>
            <div class="motto">Digital Governance Framework</div>
        </div>
        <div class="nav-right">
            <a href="#" class="nav-link">Platform</a>
            <a href="#" class="nav-link">Intelligence</a>
            <a href="#" class="nav-link">Contact</a>
        </div>
    </nav>

    <header class="hero">
        <h1>We architect digital legacies.</h1>
        <p>A global infrastructure designed for high-level oversight, systemic integrity, and the future of management technology.</p>
        <div class="hero-btns">
            <button class="btn-black">View Ecosystem</button>
            <button class="btn-outline">Our Philosophy</button>
        </div>
    </header>

    <main>
        <section class="content-section">
            <div class="section-header">
                <h2>Structural Foundations</h2>
                <p>The core principles that define our approach to organizational technology.</p>
            </div>
            <div class="card-grid">
                <div class="info-card">
                    <div class="card-icon">◈</div>
                    <div class="card-mid">Clarity</div>
                    <div class="card-desc">Eliminating systemic noise to provide a crystal-clear view of operational performance and data flows.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">⬢</div>
                    <div class="card-mid">Precision</div>
                    <div class="card-desc">Engineering tools that respond with exact accuracy, ensuring no margin for error in critical decision-making.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">✦</div>
                    <div class="card-mid">Integrity</div>
                    <div class="card-desc">Maintaining the highest standards of security and structural coherence within every node of the system.</div>
                </div>
            </div>
        </section>

        <section class="content-section" style="background: #fafafa; border-top: 1px solid var(--border); border-bottom: 1px solid var(--border); width: 100%; max-width: none;">
            <div class="section-header">
                <h2>Our Mission</h2>
                <p>Driving the evolution of digital oversight and governance through innovation.</p>
            </div>
            <div class="card-grid" style="max-width: 1200px;">
                <div class="info-card">
                    <div class="card-icon">⏀</div>
                    <div class="card-mid">Global Reach</div>
                    <div class="card-desc">To provide every modern enterprise with a unified interface to control their global digital footprint.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">⩇</div>
                    <div class="card-mid">Future Proof</div>
                    <div class="card-desc">Anticipating the needs of the 2030 digital economy through proactive architectural updates today.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">⧉</div>
                    <div class="card-mid">Accessibility</div>
                    <div class="card-desc">Democratizing complex data management by making high-level tools intuitive and easy to master.</div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="f-container">
            <div class="f-col">
                <div class="brand">SLEEK OS</div>
                <p style="margin-top: 10px;">Redefining the boundaries of digital governance and strategic oversight. Crafted for the modern overseer.</p>
            </div>
            <div class="f-col">
                <h4>Information</h4>
                <a href="#">Know More</a>
                <a href="#">Support Center</a>
                <a href="#">System FAQs</a>
                <a href="#">Privacy Policy</a>
            </div>
            <div class="f-col">
                <h4>Connect</h4>
                <p>128 Axis Plaza, Lagos, NG</p>
                <p>+234 800 123 4567</p>
                <p>governance@sleekos.io</p>
            </div>
        </div>
        <div class="f-bottom">
            &copy; 2026 SLEEK OS STUDIO. ALL RIGHTS RESERVED.
        </div>
    </footer>

</body>
</html>""",
    "Sleek Profile Page": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile | Sleek OS</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fcfcfc;
            --surface: #ffffff;
            --black: #000000;
            --muted: #888888;
            --border: #eeeeee;
            --accent: #0070f3;
            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--black); line-height: 1.6; }

        /* --- NAVIGATION --- */
        nav {
            display: flex; justify-content: space-between; align-items: center;
            padding: 1.5rem 5%; background: var(--surface); border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 1000;
        }
        .nav-left .brand { font-weight: 700; font-size: 1.1rem; letter-spacing: 1px; line-height: 1.2; }
        .nav-left .motto { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1.5px; }
        .nav-right { display: flex; gap: 2rem; }
        .nav-link { text-decoration: none; color: var(--muted); font-size: 0.85rem; font-weight: 500; transition: var(--transition); }
        .nav-link:hover { color: var(--black); }

        /* --- HERO SECTION --- */
        .hero {
            padding: 6rem 5% 4rem; text-align: center; max-width: 900px; margin: 0 auto;
            display: flex; flex-direction: column; align-items: center;
        }
        .hero h1 { font-size: clamp(2rem, 6vw, 3.5rem); font-weight: 700; letter-spacing: -1.5px; margin-bottom: 1.5rem; }
        .hero p { font-size: 1rem; color: var(--muted); margin-bottom: 2rem; max-width: 550px; }
        .hero-btns { display: flex; gap: 1rem; }
        .btn-black { padding: 0.8rem 2rem; background: var(--black); color: white; border: none; font-size: 0.8rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-outline { padding: 0.8rem 2rem; border: 1px solid var(--border); background: transparent; font-size: 0.8rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
        .btn-black:hover { opacity: 0.8; transform: translateY(-2px); }

        /* --- USER BODY --- */
        .profile-container {
            max-width: 800px; margin: 0 auto 6rem; padding: 0 5%;
            display: flex; flex-direction: column; align-items: center; text-align: center;
        }
        .profile-pic {
            width: 120px; height: 120px; border-radius: 50%;
            background: #eee; border: 4px solid var(--surface);
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 1.5rem;
            object-fit: cover;
        }
        .username { font-size: 1.5rem; font-weight: 700; letter-spacing: -0.5px; }
        .status-badge {
            display: inline-block; padding: 4px 12px; border-radius: 20px;
            font-size: 0.65rem; font-weight: 700; text-transform: uppercase;
            background: #e6fffa; color: #2c7a7b; margin: 0.5rem 0 1.5rem;
        }
        .user-stats {
            display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;
            width: 100%; padding: 2rem; border: 1px solid var(--border); background: white;
        }
        .stat-item span { display: block; font-size: 0.7rem; color: var(--muted); text-transform: uppercase; margin-bottom: 5px; }
        .stat-item strong { font-size: 1.2rem; font-weight: 600; }

        /* --- SECTION 1: ACTIVITY CARDS --- */
        .content-section {
            padding: 6rem 5%; max-width: 1100px; margin: 0 auto;
            text-align: center; border-top: 1px solid var(--border);
        }
        .section-header { margin-bottom: 3.5rem; }
        .section-header h2 { font-size: 1.8rem; font-weight: 700; margin-bottom: 0.5rem; }
        .section-header p { color: var(--muted); font-size: 0.9rem; }

        .card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; width: 100%; }
        .info-card {
            background: var(--surface); border: 1px solid var(--border);
            padding: 3rem 1.5rem; transition: var(--transition);
            display: flex; flex-direction: column; align-items: center;
        }
        .info-card:hover { border-color: var(--black); transform: translateY(-5px); }
        .card-icon { font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--black); }
        .card-mid { font-size: 1.1rem; font-weight: 600; margin-bottom: 1rem; }
        .card-desc { font-size: 0.85rem; color: var(--muted); }

        /* --- FOOTER --- */
        footer {
            padding: 6rem 5% 2rem; background: var(--surface); border-top: 1px solid var(--border);
        }
        .f-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4rem; margin-bottom: 4rem; }
        .f-col .brand { font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }
        .f-col h4 { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1.5rem; }
        .f-col p, .f-col a { font-size: 0.85rem; color: var(--muted); text-decoration: none; display: block; margin-bottom: 0.8rem; }
        
        .f-bottom {
            padding-top: 2rem; border-top: 1px solid var(--border);
            text-align: center; font-size: 0.7rem; color: var(--muted); letter-spacing: 1px;
        }

        @media (max-width: 900px) {
            .card-grid, .f-container, .user-stats { grid-template-columns: 1fr; }
            .hero h1 { font-size: 2.2rem; }
        }
    </style>
</head>
<body>

    <nav>
        <div class="nav-left">
            <div class="brand">SLEEK OS</div>
            <div class="motto">Overseer Management Suite</div>
        </div>
        <div class="nav-right">
            <a href="#" class="nav-link">Dashboard</a>
            <a href="#" class="nav-link">Settings</a>
            <a href="#" class="nav-link">Logout</a>
        </div>
    </nav>

    <header class="hero">
        <h1>Personal Command Center</h1>
        <p>Manage your identity, track systemic contributions, and oversee your directorial credentials in real-time.</p>
        <div class="hero-btns">
            <button class="btn-black">Edit Profile</button>
            <button class="btn-outline">Download Data</button>
        </div>
    </header>

    <main>
        <div class="profile-container">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Alexander" alt="User Profile" class="profile-pic">
            <div class="username">Alexander Rivera</div>
            <div class="status-badge">Principal Overseer</div>
            
            <div class="user-stats">
                <div class="stat-item">
                    <span>Forms Completed</span>
                    <strong>1,284</strong>
                </div>
                <div class="stat-item">
                    <span>Security Clearance</span>
                    <strong>Level 09</strong>
                </div>
                <div class="stat-item">
                    <span>Account Age</span>
                    <strong>742 Days</strong>
                </div>
            </div>
        </div>

        <section class="content-section">
            <div class="section-header">
                <h2>Contribution Metrics</h2>
                <p>An overview of your recent operational impact and systemic health.</p>
            </div>
            <div class="card-grid">
                <div class="info-card">
                    <div class="card-icon">⌘</div>
                    <div class="card-mid">System Stability</div>
                    <div class="card-desc">Your recent governance actions have maintained a 98% uptime across all assigned nodes.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">◈</div>
                    <div class="card-mid">Policy Audits</div>
                    <div class="card-desc">You have successfully reviewed 42 high-level policies within the current directorial cycle.</div>
                </div>
                <div class="info-card">
                    <div class="card-icon">⏀</div>
                    <div class="card-mid">Resource Flow</div>
                    <div class="card-desc">Your bandwidth allocation strategies have reduced latency by 14% this quarter.</div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="f-container">
            <div class="f-col">
                <div class="brand">SLEEK OS</div>
                <p>Defining the standard of digital governance. Built for precision and strategic clarity.</p>
            </div>
            <div class="f-col">
                <h4>Information</h4>
                <a href="#">Know More</a>
                <a href="#">Support Center</a>
                <a href="#">System FAQs</a>
            </div>
            <div class="f-col">
                <h4>Contact</h4>
                <p>128 Axis Plaza, Lagos, NG</p>
                <p>+234 800 123 4567</p>
                <p>profile@sleekos.io</p>
            </div>
        </div>
        <div class="f-bottom">
            &copy; 2026 SLEEK OS STUDIO. ALL RIGHTS RESERVED.
        </div>
    </footer>

</body>
</html>""",
}

def load_template(recursive: bool = True):
    action = int(input("Select a template to Load (1-4):\n1. Sleek Sign Up Page\n2. Sleek Sign In Page\n3. Sleek About Page\n4. Sleek Profile Page\n5. Load All Templates > "))

    if action < 5:
        template_name = list(TEMPLATES.keys())[action - 1]
        print(f"Loading template: {template_name}")
        print(f"Saving to: {f"G:\\code\\QAP\\pages-Overview\\{template_name}.html"}...")
        with open(f"G:\\code\\QAP\\pages-Overview\\{template_name}.html", "w") as f:
            f.write(TEMPLATES[template_name])
        print(f"Saved to: {template_name}.html")
    elif action == 5:
        for template_name in TEMPLATES.keys():
            print(f"Loading template: {template_name}")
            print(f"Saving to: {f"G:\\code\\QAP\\pages-Overview\\{template_name}.html"}...")
            try:
                with open(f"G:\\code\\QAP\\pages-Overview\\{template_name}.html", "w") as f:
                    f.write(TEMPLATES[template_name])
                print(f"Saved to: {template_name}.html")
            except Exception as e:
                continue
                print(f"Error saving {template_name}: {e}")
    else:
        print("Invalid selection. Please choose a number between 1 and 5.")
        if recursive: load_template()

load_template()