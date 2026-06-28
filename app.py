import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="DirectMaster — Обучение Яндекс.Директу",
    page_icon="🚀",
    layout="wide"
)

# УБИРАЕМ ОТСТУПЫ STREAMLIT
st.markdown("""
<style>
    .main > div { padding: 0 !important; max-width: 100% !important; width: 100% !important; }
    .stApp { margin: 0 !important; padding: 0 !important; background: transparent !important; }
    .stAppViewContainer { padding: 0 !important; margin: 0 !important; background: transparent !important; width: 100% !important; }
    .st-emotion-cache-1v0mbdj { padding: 0 !important; margin: 0 !important; width: 100% !important; }
    .st-emotion-cache-16idsys { padding: 0 !important; margin: 0 !important; width: 100% !important; }
    header, footer, #MainMenu, .stDeployButton, .stToolbar { display: none !important; }
    ::-webkit-scrollbar { width: 0px !important; background: transparent !important; }
    .stAppViewContainer > section { padding: 0 !important; margin: 0 !important; width: 100vw !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DirectMaster — Обучение Яндекс.Директу</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: "Inter", sans-serif;
            background: #0b0d15;
            color: #f0f4ff;
            overflow-x: hidden;
            margin: 0 !important;
            padding: 0 !important;
            width: 100% !important;
            min-height: 100vh;
        }

        .gradient-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -2;
            background: radial-gradient(circle at 20% 30%, #1a1f35, #0b0d15 70%);
        }
        .gradient-bg::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 80% 70%, #2d1b4e, transparent 50%),
                        radial-gradient(circle at 30% 80%, #1a3a4a, transparent 40%);
            animation: ambientMove 20s ease-in-out infinite alternate;
            z-index: -1;
        }
        @keyframes ambientMove {
            0% { transform: scale(1) rotate(0deg); opacity: 0.6; }
            100% { transform: scale(1.2) rotate(5deg); opacity: 1; }
        }

        #particles-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 0;
            pointer-events: none;
        }

        #cursor-glow {
            position: fixed;
            width: 250px;
            height: 250px;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            background: radial-gradient(circle, rgba(167,139,250,0.10) 0%, rgba(96,165,250,0.04) 40%, transparent 70%);
            transform: translate(-50%, -50%);
            transition: width 0.4s, height 0.4s;
            mix-blend-mode: screen;
        }
        #cursor-glow.hover { width: 350px; height: 350px; background: radial-gradient(circle, rgba(167,139,250,0.18) 0%, rgba(96,165,250,0.08) 40%, transparent 70%); }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 30px;
            position: relative;
            z-index: 2;
            min-height: 100vh;
            padding-bottom: 40px;
        }
        .reveal { opacity: 0; transform: translateY(60px) scale(0.96); transition: all 0.9s cubic-bezier(0.23, 1, 0.32, 1); }
        .reveal.visible { opacity: 1; transform: translateY(0) scale(1); }

        /* ===== НАВИГАЦИЯ ===== */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 28px 0;
            border-bottom: 1px solid rgba(255,255,255,0.04);
            flex-wrap: wrap;
        }
        .logo {
            font-weight: 700;
            font-size: 1.8rem;
            background: linear-gradient(135deg, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .logo svg { width: 32px; height: 32px; stroke: #a78bfa; fill: none; stroke-width: 1.8; }
        .nav-cta {
            background: rgba(255,255,255,0.04);
            padding: 12px 28px;
            border-radius: 60px;
            font-weight: 500;
            font-size: 0.95rem;
            border: 1px solid rgba(255,255,255,0.06);
            transition: all 0.3s;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            letter-spacing: 0.3px;
        }
        .nav-cta:hover { background: rgba(255,255,255,0.08); transform: scale(1.02); border-color: #a78bfa; }
        .nav-cta svg { width: 18px; height: 18px; stroke: #c4b5fd; fill: none; stroke-width: 2; }

        /* ===== HERO ===== */
        .hero {
            padding: 60px 0 50px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 25px;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(167,139,250,0.08);
            padding: 10px 28px;
            border-radius: 60px;
            font-size: 0.9rem;
            font-weight: 500;
            color: #c4b5fd;
            border: 1px solid rgba(167,139,250,0.1);
            backdrop-filter: blur(4px);
            width: fit-content;
            animation: pulseBadge 4s infinite;
        }
        .hero-badge svg { width: 18px; height: 18px; stroke: #c4b5fd; fill: none; stroke-width: 2; }
        @keyframes pulseBadge {
            0% { box-shadow: 0 0 0 0 rgba(167,139,250,0.1); }
            50% { box-shadow: 0 0 0 15px rgba(167,139,250,0); }
            100% { box-shadow: 0 0 0 0 rgba(167,139,250,0.1); }
        }
        .hero h1 {
            font-size: clamp(2.8rem, 10vw, 5.2rem);
            font-weight: 800;
            line-height: 1.05;
            max-width: 900px;
            margin: 0 auto;
        }
        .hero h1 span {
            background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-desc {
            font-size: 1.25rem;
            color: #94a3b8;
            max-width: 620px;
            font-weight: 400;
            line-height: 1.7;
            margin: 0 auto;
        }
        .hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: 18px;
            margin-top: 10px;
            justify-content: center;
        }

        .btn-primary {
            background: linear-gradient(135deg, #7c3aed, #4f46e5);
            padding: 18px 48px;
            border-radius: 80px;
            font-weight: 600;
            font-size: 1.1rem;
            border: none;
            color: white;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 8px 30px -6px rgba(124,58,237,0.4);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 12px;
        }
        .btn-primary:hover { transform: translateY(-4px) scale(1.02); box-shadow: 0 18px 40px -8px rgba(124,58,237,0.6); }
        .btn-secondary {
            background: rgba(255,255,255,0.04);
            padding: 18px 40px;
            border-radius: 80px;
            font-weight: 500;
            font-size: 1.05rem;
            border: 1px solid rgba(255,255,255,0.08);
            color: #e2e8f0;
            cursor: pointer;
            transition: all 0.3s;
            backdrop-filter: blur(4px);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }
        .btn-secondary:hover { background: rgba(255,255,255,0.08); transform: translateY(-3px); border-color: #a78bfa; }

        /* ===== ТАЙМЕР ===== */
        .timer-section {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0 15px;
            flex-wrap: wrap;
        }
        .timer-item {
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px;
            padding: 16px 28px;
            text-align: center;
            min-width: 80px;
        }
        .timer-item .number {
            font-size: 2.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: block;
            line-height: 1.2;
        }
        .timer-item .label {
            font-size: 0.8rem;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        /* ===== ПЛАШКА С МЕСТАМИ ===== */
        .places-bar {
            background: rgba(255,255,255,0.04);
            border-radius: 60px;
            padding: 16px 30px;
            display: flex;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
            border: 1px solid rgba(255,255,255,0.06);
            max-width: 500px;
            margin: 0 auto;
            backdrop-filter: blur(10px);
        }
        .places-bar .bar-track {
            flex: 1;
            min-width: 120px;
            height: 6px;
            background: rgba(255,255,255,0.06);
            border-radius: 10px;
            overflow: hidden;
        }
        .places-bar .bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #7c3aed, #a78bfa);
            border-radius: 10px;
            width: 86%;
            animation: barPulse 2s ease-in-out infinite;
        }
        @keyframes barPulse {
            0% { opacity: 0.8; }
            50% { opacity: 1; }
            100% { opacity: 0.8; }
        }
        .places-bar .places-text {
            font-size: 0.95rem;
            font-weight: 500;
            white-space: nowrap;
            color: #e2e8f0;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .places-bar .places-text span { color: #a78bfa; font-weight: 700; }

        /* ===== СТАТИСТИКА ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 30px;
            margin: 40px 0 30px;
        }
        .stat-item {
            text-align: center;
            padding: 30px 20px;
            background: rgba(255,255,255,0.02);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.04);
            transition: all 0.3s;
        }
        .stat-item:hover { background: rgba(255,255,255,0.06); transform: translateY(-6px); border-color: rgba(167,139,250,0.2); }
        .stat-number {
            font-size: 3.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: block;
        }
        .stat-label {
            color: #94a3b8;
            font-size: 1rem;
            margin-top: 6px;
        }

        /* ===== ПРЕИМУЩЕСТВА ===== */
        .grid-3 {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin: 50px 0 70px;
            justify-items: center;
        }
        .feature-card {
            padding: 40px 30px;
            transition: all 0.4s;
            border-radius: 2rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.04);
            text-align: center;
            width: 100%;
            max-width: 360px;
            cursor: pointer;
            position: relative;
        }
        .feature-card:hover {
            transform: translateY(-12px);
            background: rgba(255,255,255,0.06);
            border-color: rgba(167,139,250,0.3);
            box-shadow: 0 30px 60px -20px rgba(0,0,0,0.7);
        }
        .feature-icon {
            width: 64px;
            height: 64px;
            margin: 0 auto 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(167,139,250,0.06);
            border-radius: 16px;
            padding: 14px;
            border: 1px solid rgba(167,139,250,0.05);
        }
        .feature-icon svg { width: 32px; height: 32px; stroke: #a78bfa; fill: none; stroke-width: 1.8; }
        .feature-card h3 { font-size: 1.5rem; font-weight: 600; margin-bottom: 12px; }
        .feature-card p { color: #94a3b8; font-weight: 300; }

        /* ===== БЛОК ПОТОКА ===== */
        .stream-block {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            background: rgba(255,255,255,0.02);
            border-radius: 20px;
            padding: 24px 36px;
            border: 1px solid rgba(255,255,255,0.04);
            margin: 20px 0 30px;
        }
        .stream-block .date {
            font-size: 1.3rem;
            font-weight: 700;
            color: #f0f4ff;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .stream-block .date span { color: #a78bfa; }

        /* ===== ГРАФИК ===== */
        .chart-container {
            background: rgba(255,255,255,0.02);
            border-radius: 24px;
            padding: 30px 30px 20px;
            border: 1px solid rgba(255,255,255,0.04);
            margin: 20px auto 50px;
            max-width: 600px;
        }
        .chart-bars {
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            height: 120px;
            gap: 12px;
        }
        .chart-bar-item {
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 6px;
        }
        .chart-bar {
            width: 100%;
            max-width: 40px;
            border-radius: 8px 8px 4px 4px;
            background: linear-gradient(180deg, #a78bfa, #4f46e5);
            height: 10px;
            min-height: 10px;
        }
        .chart-bar-item:nth-child(1) .chart-bar { height: 30px; }
        .chart-bar-item:nth-child(2) .chart-bar { height: 50px; }
        .chart-bar-item:nth-child(3) .chart-bar { height: 70px; }
        .chart-bar-item:nth-child(4) .chart-bar { height: 95px; }
        .chart-bar-item:nth-child(5) .chart-bar { height: 80px; }
        .chart-bar-item:nth-child(6) .chart-bar { height: 110px; }
        .chart-bar-label {
            font-size: 0.65rem;
            color: #94a3b8;
            text-align: center;
        }

        /* ===== КАЛЬКУЛЯТОР ===== */
        .calculator {
            max-width: 560px;
            margin: 0 auto 50px;
            background: rgba(255,255,255,0.02);
            border-radius: 24px;
            padding: 32px 36px;
            border: 1px solid rgba(255,255,255,0.04);
        }
        .calculator label {
            display: block;
            font-weight: 500;
            margin-bottom: 8px;
            color: #e2e8f0;
        }
        .calculator .input-row {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(255,255,255,0.04);
            border-radius: 12px;
            padding: 0 16px;
            border: 1px solid rgba(255,255,255,0.06);
        }
        .calculator input[type="range"] {
            -webkit-appearance: none;
            flex: 1;
            height: 4px;
            background: rgba(255,255,255,0.08);
            border-radius: 10px;
            outline: none;
        }
        .calculator input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #a78bfa);
            cursor: pointer;
            box-shadow: 0 0 20px rgba(124,58,237,0.3);
        }
        .calculator .result-row {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.04);
            flex-wrap: wrap;
            gap: 12px;
        }
        .calculator .result-item {
            text-align: center;
            flex: 1;
            min-width: 80px;
        }
        .calculator .result-item .value {
            font-size: 1.6rem;
            font-weight: 700;
            background: linear-gradient(135deg, #a78bfa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: block;
        }
        .calculator .result-item .label {
            font-size: 0.8rem;
            color: #94a3b8;
        }

        /* ===== ПАРТНЁРСКИЙ БЕЙДЖ ===== */
        .partner-badge {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(167,139,250,0.06);
            padding: 8px 20px;
            border-radius: 60px;
            border: 1px solid rgba(167,139,250,0.08);
            font-size: 0.8rem;
            color: #c4b5fd;
        }

        /* ===== ТАРИФЫ ===== */
        .pricing-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            justify-content: center;
            margin: 50px 0 60px;
        }
        .pricing-card {
            flex: 1 1 280px;
            max-width: 360px;
            padding: 40px 32px;
            text-align: center;
            transition: all 0.4s;
            border-radius: 2.5rem;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.04);
            cursor: pointer;
            position: relative;
        }
        .pricing-card.popular {
            border-color: #7c3aed;
            background: rgba(124,58,237,0.04);
            transform: scale(1.02);
        }
        .pricing-card.popular::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #7c3aed, #a78bfa, #7c3aed);
            background-size: 200% 100%;
            animation: progressLine 3s linear infinite;
        }
        @keyframes progressLine {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        .pricing-card:hover { transform: translateY(-10px); background: rgba(255,255,255,0.06); }
        .pricing-card.popular:hover { transform: scale(1.04) translateY(-6px); }
        .popular-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #7c3aed;
            padding: 6px 18px;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 12px;
            color: white;
        }
        .price {
            font-size: 3.4rem;
            font-weight: 800;
            margin: 20px 0 10px;
        }
        .price small { font-size: 1.2rem; font-weight: 400; color: #94a3b8; }
        .pricing-card ul {
            list-style: none;
            margin: 30px 0;
            text-align: left;
        }
        .pricing-card ul li {
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.03);
            display: flex;
            align-items: center;
            gap: 12px;
            color: #e2e8f0;
        }
        .pricing-card ul li::before { content: "✦"; color: #a78bfa; font-size: 1rem; }
        .pricing-card .btn-primary { width: 100%; justify-content: center; padding: 14px; }

        /* ===== ПОДВАЛ ===== */
        .footer {
            border-top: 1px solid rgba(255,255,255,0.04);
            padding: 40px 0;
            margin-top: 60px;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
            color: #6b7a9f;
            font-size: 0.95rem;
            text-align: center;
        }
        .footer-links { display: flex; gap: 24px; }
        .footer a { color: #6b7a9f; text-decoration: none; transition: color 0.3s; cursor: pointer; }
        .footer a:hover { color: #a78bfa; }

        /* ===== РЕЙТИНГ ===== */
        .rating-block {
            display: flex;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 30px 0 50px;
        }
        .rating-block .big-number {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(135deg, #a78bfa, #60a5fa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .rating-block .stars-row {
            display: flex;
            gap: 4px;
        }
        .rating-block .stars-row svg {
            width: 24px;
            height: 24px;
            fill: #a78bfa;
            stroke: #7c3aed;
            stroke-width: 0.5;
        }
        .rating-block .rating-bar {
            flex: 1;
            min-width: 120px;
            height: 4px;
            background: rgba(255,255,255,0.06);
            border-radius: 10px;
            overflow: hidden;
        }
        .rating-block .rating-bar .fill {
            height: 100%;
            width: 98%;
            background: linear-gradient(90deg, #7c3aed, #a78bfa);
            border-radius: 10px;
        }

        /* ===== ОТЗЫВЫ ===== */
        .reviews-slider {
            display: flex;
            gap: 30px;
            overflow-x: auto;
            padding: 20px 0 40px;
            scroll-snap-type: x mandatory;
            scrollbar-width: none;
        }
        .reviews-slider::-webkit-scrollbar { display: none; }
        .review-card {
            flex: 0 0 320px;
            scroll-snap-align: start;
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.04);
            border-radius: 24px;
            padding: 30px 28px;
            transition: all 0.3s;
        }
        .review-card:hover { transform: translateY(-8px); background: rgba(255,255,255,0.06); border-color: rgba(167,139,250,0.2); }
        .review-stars {
            display: flex;
            gap: 6px;
            margin-bottom: 14px;
        }
        .review-stars svg {
            width: 22px;
            height: 22px;
            fill: #a78bfa;
            stroke: #7c3aed;
            stroke-width: 0.5;
        }
        .review-text {
            color: #e2e8f0;
            font-size: 0.95rem;
            line-height: 1.7;
            margin-bottom: 16px;
            font-style: italic;
        }
        .review-author {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .review-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #4f46e5);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 1.2rem;
            color: white;
            flex-shrink: 0;
        }
        .review-name { font-weight: 600; font-size: 0.95rem; }
        .review-role { color: #94a3b8; font-size: 0.8rem; }

        /* ===== FAQ ===== */
        .faq-list {
            max-width: 800px;
            margin: 0 auto 50px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }
        .faq-item {
            background: rgba(255,255,255,0.02);
            border: 1px solid rgba(255,255,255,0.04);
            border-radius: 16px;
            overflow: hidden;
            transition: all 0.3s;
        }
        .faq-item:hover { background: rgba(255,255,255,0.04); border-color: rgba(167,139,250,0.1); }
        .faq-question {
            width: 100%;
            padding: 20px 28px;
            background: none;
            border: none;
            color: #f0f4ff;
            font-size: 1.05rem;
            font-weight: 500;
            text-align: left;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: inherit;
            transition: all 0.3s;
        }
        .faq-question:hover { color: #a78bfa; }
        .faq-question .icon {
            font-size: 1.4rem;
            transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            color: #a78bfa;
            flex-shrink: 0;
            margin-left: 16px;
        }
        .faq-item.open .faq-question .icon { transform: rotate(45deg); }
        .faq-answer {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.4s ease, padding 0.3s ease;
            padding: 0 28px;
            color: #b0b9d4;
            line-height: 1.7;
        }
        .faq-item.open .faq-answer { max-height: 200px; padding: 0 28px 24px; }

        /* ===== АДАПТИВ ===== */
        @media (max-width: 700px) {
            .container { padding: 0 15px; }
            .navbar { flex-direction: column; gap: 18px; align-items: center; text-align: center; }
            .hero { padding: 40px 0 30px; }
            .hero h1 { font-size: 2.4rem; }
            .hero-desc { font-size: 1.05rem; }
            .pricing-card.popular { transform: scale(1); }
            .pricing-card.popular:hover { transform: translateY(-6px); }
            .footer { flex-direction: column; align-items: center; }
            .footer-links { justify-content: center; }
            #cursor-glow { display: none; }
            .timer-item .number { font-size: 2rem; }
            .stat-number { font-size: 2.4rem; }
            .calculator { padding: 24px 18px; }
            .places-bar { padding: 12px 20px; flex-direction: column; gap: 10px; }
            .review-card { flex: 0 0 280px; }
            .chart-container { padding: 20px 16px; }
            .chart-bars { height: 80px; gap: 6px; }
        }
    </style>
</head>
<body>
    <canvas id="particles-canvas"></canvas>

    <svg style="position: absolute; width: 0; height: 0;">
        <defs>
            <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#a78bfa"/>
                <stop offset="100%" stop-color="#60a5fa"/>
            </linearGradient>
            <linearGradient id="iconGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#a78bfa"/>
                <stop offset="100%" stop-color="#818cf8"/>
            </linearGradient>
        </defs>
    </svg>

    <div id="cursor-glow"></div>
    <div class="gradient-bg"></div>

    <div class="container">
        <!-- НАВИГАЦИЯ -->
        <nav class="navbar">
            <div class="logo">
                <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                    <path d="M2 17l10 5 10-5"/>
                    <path d="M2 12l10 5 10-5"/>
                </svg>
                DirectMaster
            </div>
            <div class="nav-cta">
                <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                    <path d="M2 17l10 5 10-5"/>
                    <path d="M2 12l10 5 10-5"/>
                    <path d="M12 2v22"/>
                </svg>
                Старт 15 июля
            </div>
        </nav>

        <!-- HERO -->
        <section class="hero reveal">
            <span class="hero-badge">
                <svg viewBox="0 0 24 24" fill="none" stroke="#c4b5fd" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                </svg>
                Набор закрывается через
            </span>

            <div class="timer-section" id="timer">
                <div class="timer-item"><span class="number" id="timer-days">00</span><span class="label">Дней</span></div>
                <div class="timer-item"><span class="number" id="timer-hours">00</span><span class="label">Часов</span></div>
                <div class="timer-item"><span class="number" id="timer-minutes">00</span><span class="label">Минут</span></div>
                <div class="timer-item"><span class="number" id="timer-seconds">00</span><span class="label">Секунд</span></div>
            </div>

            <div class="places-bar">
                <span class="places-text">
                    <svg width="18" height="18" viewBox="0 0 24 24" stroke="#f97316" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 8v4l3 3"/>
                    </svg>
                    Осталось <span id="places-count">7</span> мест из 50
                </span>
                <div class="bar-track"><div class="bar-fill" style="width: 86%;"></div></div>
            </div>

            <h1>Стань <span>экспертом</span> по Яндекс.Директу за 4 недели</h1>
            <p class="hero-desc">Практический онлайн-курс с живыми кейсами, разбором реальных кампаний и стратегиями, которые приносят прибыль.</p>
            <div class="hero-actions">
                <a href="#" class="btn-primary">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14"/><path d="M12 5l7 7-7 7"/>
                    </svg>
                    Записаться на курс
                </a>
                <a href="#" class="btn-secondary">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polygon points="5 3 19 12 5 21 5 3"/>
                    </svg>
                    Смотреть программу
                </a>
            </div>
        </section>

        <!-- БЛИЖАЙШИЙ ПОТОК -->
        <div class="stream-block reveal">
            <div class="date">
                <svg width="24" height="24" viewBox="0 0 24 24" stroke="#a78bfa" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                    <line x1="16" y1="2" x2="16" y2="6"/>
                    <line x1="8" y1="2" x2="8" y2="6"/>
                    <line x1="3" y1="10" x2="21" y2="10"/>
                    <circle cx="12" cy="15" r="1"/>
                </svg>
                Ближайший поток: <span>15 июля 2026</span>
            </div>
            <a href="#" class="btn-primary" style="padding: 12px 28px; font-size: 0.95rem;">Напомнить</a>
        </div>

        <!-- СТАТИСТИКА -->
        <div style="text-align: center; margin: 40px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Нам доверяют</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Результаты наших учеников говорят сами за себя</p>
        </div>
        <div class="stats-grid">
            <div class="stat-item reveal">
                <span class="stat-number" data-target="500">0</span>
                <span class="stat-label">+ учеников</span>
            </div>
            <div class="stat-item reveal">
                <span class="stat-number" data-target="95">0</span>
                <span class="stat-label">% успешных запусков</span>
            </div>
            <div class="stat-item reveal">
                <span class="stat-number" data-target="50">0</span>
                <span class="stat-label">+ ниш</span>
            </div>
            <div class="stat-item reveal">
                <span class="stat-number" data-target="4.9">0</span>
                <span class="stat-label">⭐ средний рейтинг</span>
            </div>
        </div>

        <!-- ГРАФИК -->
        <div class="chart-container reveal" style="margin: 20px auto 50px;">
            <div style="text-align:center; font-weight:600; margin-bottom:20px; color:#e2e8f0; display:flex; align-items:center; justify-content:center; gap:10px;">
                <svg width="22" height="22" viewBox="0 0 24 24" stroke="#34d399" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                    <polyline points="17 6 23 6 23 12"/>
                </svg>
                Рост среднего дохода учеников после курса
            </div>
            <div class="chart-bars">
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 1</span></div>
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 2</span></div>
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 3</span></div>
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 4</span></div>
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 5</span></div>
                <div class="chart-bar-item"><div class="chart-bar"></div><span class="chart-bar-label">Месяц 6</span></div>
            </div>
        </div>

        <!-- ПАРТНЁР -->
        <div style="text-align: center; margin: 20px 0 40px;">
            <span class="partner-badge">
                <svg width="20" height="20" viewBox="0 0 24 24" stroke="#a78bfa" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    <polyline points="9 12 11 14 15 10"/>
                </svg>
                Официальный партнёр Яндекс
            </span>
        </div>

        <!-- ПРЕИМУЩЕСТВА -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Ключевые преимущества</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Что ты получишь на курсе</p>
        </div>
        <div class="grid-3">
            <div class="feature-card reveal">
                <div class="feature-icon">
                    <svg viewBox="0 0 24 24" stroke="url(#iconGrad)" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 12v-2a5 5 0 0 0-5-5H8a5 5 0 0 0-5 5v2"/>
                        <circle cx="12" cy="16" r="5"/>
                        <path d="M12 11v5"/><path d="M9 16h6"/>
                    </svg>
                </div>
                <h3>Реальные кейсы</h3>
                <p>Разбираем кампании с бюджетом от 100 000 ₽ до 5 млн ₽ из разных ниш.</p>
            </div>
            <div class="feature-card reveal">
                <div class="feature-icon">
                    <svg viewBox="0 0 24 24" stroke="url(#iconGrad)" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="2" width="20" height="20" rx="2.18"/>
                        <line x1="8" y1="2" x2="8" y2="22"/><line x1="16" y1="2" x2="16" y2="22"/>
                        <line x1="2" y1="8" x2="22" y2="8"/><line x1="2" y1="16" x2="22" y2="16"/>
                    </svg>
                </div>
                <h3>Автоматизация</h3>
                <p>Настройка скриптов, стратегий и работы с API — сделаем из тебя инженера.</p>
            </div>
            <div class="feature-card reveal">
                <div class="feature-icon">
                    <svg viewBox="0 0 24 24" stroke="url(#iconGrad)" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 6v6l4 2"/>
                    </svg>
                </div>
                <h3>Только практика</h3>
                <p>Ты создашь и запустишь рекламную кампанию с нуля под нашим контролем.</p>
            </div>
        </div>

        <!-- РЕЙТИНГ -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Наш рейтинг</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Оценка учеников на основе 150+ отзывов</p>
        </div>
        <div class="rating-block reveal">
            <div class="big-number">4.9</div>
            <div class="stars-row">
                <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <div class="rating-bar"><div class="fill"></div></div>
            <span style="color: #94a3b8; font-size: 0.9rem;">98%</span>
        </div>

        <!-- КАЛЬКУЛЯТОР -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Рассчитай окупаемость</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Узнай, сколько клиентов ты получишь</p>
        </div>
        <div class="calculator reveal">
            <label>Ваш бюджет на рекламу в месяц</label>
            <div class="input-row">
                <span>₽</span>
                <input type="range" id="budgetSlider" min="10000" max="500000" value="100000" step="5000">
                <span id="budgetDisplay">100 000 ₽</span>
            </div>
            <div class="result-row">
                <div class="result-item">
                    <span class="value" id="clientsResult">~50</span>
                    <span class="label">Клиентов в месяц</span>
                </div>
                <div class="result-item">
                    <span class="value" id="profitResult">~250 000 ₽</span>
                    <span class="label">Прибыль</span>
                </div>
                <div class="result-item">
                    <span class="value" id="roiResult">~250%</span>
                    <span class="label">ROI</span>
                </div>
            </div>
        </div>

        <!-- ОТЗЫВЫ -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Что говорят ученики</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Реальные отзывы выпускников</p>
        </div>
        <div class="reviews-slider">
            <div class="review-card reveal">
                <div class="review-stars">
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <p class="review-text">"Курс полностью изменил мой подход к рекламе. Запустил свою первую кампанию и получил клиентов в первый же день!"</p>
                <div class="review-author"><div class="review-avatar">А</div><div><div class="review-name">Алексей Иванов</div><div class="review-role">CEO, IT-студия</div></div></div>
            </div>
            <div class="review-card reveal">
                <div class="review-stars">
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <p class="review-text">"До этого боялся Яндекс.Директа, но после обучения запустил рекламу и окупил вложения за 3 дня."</p>
                <div class="review-author"><div class="review-avatar">М</div><div><div class="review-name">Мария Петрова</div><div class="review-role">Маркетолог</div></div></div>
            </div>
            <div class="review-card reveal">
                <div class="review-stars">
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    <svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                </div>
                <p class="review-text">"Лучший курс по контекстной рекламе! Всё структурировано, много практики и обратной связи."</p>
                <div class="review-author"><div class="review-avatar">Д</div><div><div class="review-name">Дмитрий Смирнов</div><div class="review-role">Владелец бизнеса</div></div></div>
            </div>
        </div>

        <!-- FAQ -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Часто задаваемые вопросы</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Ответы на главные вопросы</p>
        </div>
        <div class="faq-list">
            <div class="faq-item reveal"><button class="faq-question">Что если у меня нет опыта в рекламе?<span class="icon">+</span></button><div class="faq-answer">Курс разработан как для новичков, так и для специалистов. Мы начинаем с самых основ и постепенно усложняем материал.</div></div>
            <div class="faq-item reveal"><button class="faq-question">Можно ли оплатить в рассрочку?<span class="icon">+</span></button><div class="faq-answer">Да, мы предлагаем рассрочку на 3 или 6 месяцев без переплаты. Подробности уточняйте у менеджера.</div></div>
            <div class="faq-item reveal"><button class="faq-question">Выдаёте ли вы сертификат после обучения?<span class="icon">+</span></button><div class="faq-answer">Да, после успешного прохождения курса вы получаете именной сертификат, который можно добавить в портфолио и резюме.</div></div>
            <div class="faq-item reveal"><button class="faq-question">Как долго длится обучение?<span class="icon">+</span></button><div class="faq-answer">Основной курс длится 4 недели. После этого вы получаете доступ к закрытому комьюнити и бонусным материалам.</div></div>
        </div>

        <!-- ТАРИФЫ -->
        <div style="text-align: center; margin: 60px 0 10px;">
            <h2 style="font-size: 2.6rem; font-weight: 700; margin-bottom: 16px;">Выбери свой трек</h2>
            <p style="color: #94a3b8; font-size: 1.2rem; max-width: 600px; margin: 0 auto 50px;">Подходит и новичкам, и специалистам с опытом</p>
        </div>
        <div class="pricing-wrap">
            <div class="pricing-card reveal"><h3>Стандарт</h3><div class="price">19 900 <small>₽</small></div><ul><li>12 видео-уроков</li><li>Чат с кураторами</li><li>Домашние задания с проверкой</li></ul><a href="#" class="btn-primary">Выбрать</a></div>
            <div class="pricing-card popular reveal"><span class="popular-badge"><svg width="16" height="16" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" fill="white"/></svg> Самый популярный</span><h3>Профи</h3><div class="price">34 900 <small>₽</small></div><ul><li>24 видео-урока</li><li>Личный наставник</li><li>Разбор твоей ниши</li><li>Доступ к закрытому комьюнити</li></ul><a href="#" class="btn-primary">Выбрать</a></div>
            <div class="pricing-card reveal"><h3>Бизнес</h3><div class="price">59 900 <small>₽</small></div><ul><li>Всё из Профи</li><li>Индивидуальная стратегия</li><li>Аудит текущих кампаний</li><li>3 часа личной консультации</li></ul><a href="#" class="btn-primary">Выбрать</a></div>
        </div>

        <!-- ПОДВАЛ -->
        <footer class="footer">
            <span>© 2026 DirectMaster — обучение Яндекс.Директу</span>
            <div class="footer-links"><a href="#">Политика</a><a href="#">Договор</a></div>
        </footer>
    </div>

    <script>
        // ===== ЧАСТИЦЫ =====
        (function() {
            const canvas = document.getElementById('particles-canvas');
            const ctx = canvas.getContext('2d');
            let width, height;
            let particles = [];
            const NUM_PARTICLES = 40;

            function resize() {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            class Particle {
                constructor() { this.reset(); }
                reset() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.size = Math.random() * 2 + 0.5;
                    this.speedX = (Math.random() - 0.5) * 0.3;
                    this.speedY = (Math.random() - 0.5) * 0.3;
                    this.opacity = Math.random() * 0.5 + 0.1;
                }
                update() {
                    this.x += this.speedX;
                    this.y += this.speedY;
                    if (this.x < 0 || this.x > width) this.speedX *= -1;
                    if (this.y < 0 || this.y > height) this.speedY *= -1;
                }
                draw() {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fillStyle = `rgba(167, 139, 250, ${this.opacity})`;
                    ctx.fill();
                }
            }

            for (let i = 0; i < NUM_PARTICLES; i++) particles.push(new Particle());

            function drawLines() {
                for (let i = 0; i < particles.length; i++) {
                    for (let j = i + 1; j < particles.length; j++) {
                        const dx = particles[i].x - particles[j].x;
                        const dy = particles[i].y - particles[j].y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < 150) {
                            ctx.beginPath();
                            ctx.moveTo(particles[i].x, particles[i].y);
                            ctx.lineTo(particles[j].x, particles[j].y);
                            ctx.strokeStyle = `rgba(167, 139, 250, ${0.06 * (1 - dist / 150)})`;
                            ctx.lineWidth = 0.5;
                            ctx.stroke();
                        }
                    }
                }
            }

            function animateParticles() {
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => { p.update(); p.draw(); });
                drawLines();
                requestAnimationFrame(animateParticles);
            }
            animateParticles();
        })();

        // ===== СВЕЧЕНИЕ КУРСОРА =====
        (function() {
            const glow = document.getElementById('cursor-glow');
            let mouseX = 0, mouseY = 0, glowX = 0, glowY = 0;
            document.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = e.clientY; });
            function animate() {
                glowX += (mouseX - glowX) * 0.08;
                glowY += (mouseY - glowY) * 0.08;
                glow.style.left = glowX + 'px';
                glow.style.top = glowY + 'px';
                requestAnimationFrame(animate);
            }
            animate();
            document.querySelectorAll('.btn-primary, .btn-secondary, .nav-cta, .feature-card, .pricing-card').forEach(el => {
                el.addEventListener('mouseenter', () => glow.classList.add('hover'));
                el.addEventListener('mouseleave', () => glow.classList.remove('hover'));
            });
        })();

        // ===== ТАЙМЕР =====
        (function() {
            const target = new Date('2026-07-15T00:00:00');
            function updateTimer() {
                const diff = target - new Date();
                if (diff <= 0) return;
                document.getElementById('timer-days').textContent = String(Math.floor(diff / (1000*60*60*24))).padStart(2, '0');
                document.getElementById('timer-hours').textContent = String(Math.floor((diff % (1000*60*60*24)) / (1000*60*60))).padStart(2, '0');
                document.getElementById('timer-minutes').textContent = String(Math.floor((diff % (1000*60*60)) / (1000*60))).padStart(2, '0');
                document.getElementById('timer-seconds').textContent = String(Math.floor((diff % (1000*60)) / 1000)).padStart(2, '0');
            }
            updateTimer();
            setInterval(updateTimer, 1000);
        })();

        // ===== СЧЁТЧИКИ =====
        (function() {
            const counters = document.querySelectorAll('.stat-number');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const el = entry.target;
                        const target = parseFloat(el.dataset.target);
                        const isFloat = target % 1 !== 0;
                        let current = 0;
                        const increment = target / 60;
                        const timer = setInterval(() => {
                            current += increment;
                            if (current >= target) { current = target; clearInterval(timer); }
                            el.textContent = isFloat ? current.toFixed(1) : Math.round(current);
                        }, 20);
                        observer.unobserve(el);
                    }
                });
            }, { threshold: 0.5 });
            counters.forEach(el => observer.observe(el));
        })();

        // ===== FAQ =====
        document.querySelectorAll('.faq-question').forEach(btn => {
            btn.addEventListener('click', () => btn.parentElement.classList.toggle('open'));
        });

        // ===== АНИМАЦИЯ ПОЯВЛЕНИЯ =====
        (function() {
            const reveals = document.querySelectorAll('.reveal');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('visible'); });
            }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
            reveals.forEach(el => observer.observe(el));
            document.querySelector('.hero')?.classList.add('visible');
        })();

        // ===== КАЛЬКУЛЯТОР =====
        (function() {
            const slider = document.getElementById('budgetSlider');
            const display = document.getElementById('budgetDisplay');
            const clients = document.getElementById('clientsResult');
            const profit = document.getElementById('profitResult');
            const roi = document.getElementById('roiResult');

            function updateCalc(val) {
                const budget = parseInt(val);
                display.textContent = budget.toLocaleString() + ' ₽';
                const clientCount = Math.round(budget / 2000);
                const profitAmount = Math.round(budget * 2.5);
                const roiPercent = Math.round((profitAmount / budget) * 100);
                clients.textContent = '~' + clientCount;
                profit.textContent = '~' + profitAmount.toLocaleString() + ' ₽';
                roi.textContent = '~' + roiPercent + '%';
            }

            slider.addEventListener('input', function() {
                updateCalc(this.value);
            });
            updateCalc(slider.value);
        })();

        // ===== ПРОГРЕСС-БАР МЕСТ =====
        (function() {
            const places = document.getElementById('places-count');
            let count = 7;
            setInterval(() => {
                if (count > 1) {
                    count--;
                    places.textContent = count;
                }
            }, 30000);
        })();
    </script>
</body>
</html>
"""

# 🔥 ВАЖНО: ВКЛЮЧАЕМ ПРОКРУТКУ!
components.html(HTML_TEMPLATE, height=800, scrolling=True)