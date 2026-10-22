"""
Configuração do pipeline ENEM 2025 -> BigQuery.

Padrão de URL do INEP (verificado em jan/2026):
  https://download.inep.gov.br/enem/provas_e_gabaritos/2025_PV_impresso_D{dia}_CD{caderno}.pdf
  https://download.inep.gov.br/enem/provas_e_gabaritos/2025_GB_impresso_D{dia}_CD{caderno}.pdf

Cadernos por dia (aplicação regular):
  Dia 1: CD1 Azul | CD2 Amarelo | CD3 Branco | CD4 Verde
  Dia 2: CD5 Amarelo | CD6 Cinza | CD7 Azul | CD8 Verde

Use UM caderno por dia (a numeração das questões muda de cor pra cor,
mas o conteúdo é o mesmo). Recomendo o Azul como referência.
"""

ANO = 2025
BASE = "https://download.inep.gov.br/enem/provas_e_gabaritos"

# Caderno de referência escolhido por dia (Azul)
PROVAS = {
    1: {"caderno": 1, "cor": "Azul", "areas": ["Linguagens", "Ciencias Humanas"]},
    2: {"caderno": 7, "cor": "Azul", "areas": ["Ciencias da Natureza", "Matematica"]},
}

def url_prova(dia, caderno):
    return f"{BASE}/{ANO}_PV_impresso_D{dia}_CD{caderno}.pdf"

def url_gabarito(dia, caderno):
    return f"{BASE}/{ANO}_GB_impresso_D{dia}_CD{caderno}.pdf"

# Faixas de questão por área no caderno (1 questão = 1 número)
# ENEM: 90 questões/dia. Dia1: 1-45 Linguagens (5 são de língua estrangeira), 46-90 Humanas
#       Dia2: 91-135 Natureza, 136-180 Matemática
FAIXAS_AREA = {
    1: [("Linguagens, Codigos e suas Tecnologias", 1, 45),
        ("Ciencias Humanas e suas Tecnologias", 46, 90)],
    2: [("Ciencias da Natureza e suas Tecnologias", 91, 135),
        ("Matematica e suas Tecnologias", 136, 180)],
}

# Config GCP
GCP_PROJECT   = "clientco-datalake-prd"   # ajuste se quiser
BQ_DATASET    = "enem"
BQ_TABLE      = "questoes_2025"
GCS_BUCKET    = "dev-landing-speech-to-text"  # reaproveitando bucket; ajuste
GCS_PREFIX    = "enem/2025/imagens"

# Diretórios locais
DIR_PDF   = "pdfs"
DIR_IMG   = "imagens"
DIR_OUT   = "output"
