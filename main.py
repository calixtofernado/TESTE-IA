import streamlit as st

# Configuração da página e SEO básico
st.set_page_config(
    page_title="Processamento e Automação de Dados para Pequenas Empresas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS Minimalista e Responsiva (Desktop e Mobile)
st.markdown("""
    <style>
        /* Esconde elementos padrão do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajustes de espaçamento e tipografia */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }
        
        h1, h2, h3 {
            color: #1E293B;
            font-weight: 600;
        }
        
        p, li {
            color: #334155;
            font-size: 1.05rem;
            line-height: 1.6;
        }
        
        /* Card de Destaque / Chamada */
        .hero-box {
            background-color: #F8FAFC;
            padding: 2.5rem;
            border-radius: 12px;
            border: 1px solid #E2E8F0;
            margin-bottom: 2rem;
        }
        
        /* Estilização do Botão de Contato */
        .stButton>button {
            width: 100%;
            background-color: #2563EB;
            color: white;
            font-weight: bold;
            padding: 0.75rem 1rem;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s;
        }
        
        .stButton>button:hover {
            background-color: #1D4ED8;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO / HERO SECTION ---
st.markdown("""
    <div class="hero-box">
        <h1 style="margin-bottom: 0.5rem;">Transforme Dados Brutos em Decisões Inteligentes</h1>
        <p style="font-size: 1.15rem; color: #475569;">
            Ajudamos pequenas empresas a automatizar rotinas, organizar informações e ganhar tempo para focar no crescimento do negócio.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- SEÇÃO 1: SERVIÇOS ---
st.header("Nossos Serviços")
st.write("Soluções sob medida para simplificar e otimizar os processos da sua empresa.")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Imagem 1: Adequada para Mobile e Desktop (use_container_width=True garante responsividade)
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        caption="Dashboard e Relatórios Gerenciais",
        use_container_width=True
    )
    st.subheader("Processamento e Análise de Dados")
    st.markdown("""
    * **Organização de planilhas:** Limpeza e padronização de bases de dados complexas.
    * **Dashboards Interativos:** Visualização clara de vendas, estoque e finanças.
    * **Relatórios Automatizados:** Receba indicadores cruciais sem esforço diário.
    """)

with col2:
    # Imagem 2
    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        caption="Automação de Tarefas e Rotinas",
        use_container_width=True
    )
    st.subheader("Automação de Processos")
    st.markdown("""
    * **Eliminação de tarefas manuais:** Integração de sistemas e planilhas.
    * **Extração de dados:** Coleta automática de informações na web ou sistemas internos.
    * **Aumento de produtividade:** Redução drástica de erros humanos e retrabalho.
    """)

st.markdown("---")

# --- SEÇÃO 2: POR QUE AUTOMATIZAR ---
st.header("Por que investir em processamento de dados?")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("### ⏱️ Ganho de Tempo")
    st.write("Reduza horas gastas em preenchimento manual de planilhas.")

with col_b:
    st.markdown("### 🎯 Precisão")
    st.write("Elimine falhas humanas no cálculo e transferência de dados.")

with col_c:
    st.markdown("### 📈 Escala")
    st.write("Prepare sua empresa para crescer sem aumentar custos operacionais.")

st.markdown("---")

# --- SEÇÃO 3: CONTATO E LOCALIZAÇÃO ---
st.header("Entre em Contato")
st.write("Fale conosco e entenda como podemos ajudar a sua empresa a economizar tempo e recursos.")

col_contato1, col_contato2 = st.columns([1, 1], gap="large")

with col_contato1:
    st.markdown("""
    #### Informações
    * 📍 **Atendimento:** Presencial e Online
    * 📧 **E-mail:** contato@suaempresa.com.br
    * 📱 **WhatsApp:** (00) 99999-9999
    * 🕒 **Horário:** Segunda a Sexta, das 08h às 18h
    """)
    st.info("💡 **Dica para o Google Meu Negócio:** Mantenha os mesmos horários e endereço informados na sua ficha do Google.")

with col_contato2:
    with st.form("form_contato"):
        st.subheader("Envie uma mensagem")
        nome = st.text_input("Nome / Empresa")
        email = st.text_input("E-mail ou WhatsApp")
        mensagem = st.text_area("Como podemos ajudar?")
        submit = st.form_submit_button("Enviar Mensagem")
        
        if submit:
            if nome and email and mensagem:
                st.success("Obrigado pelo contato! Retornaremos em breve.")
            else:
                st.error("Por favor, preencha todos os campos.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.85rem;'>© Processamento de Dados - Soluções Eficientes para Pequenas Empresas</p>", unsafe_allow_html=True)