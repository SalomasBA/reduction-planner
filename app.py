import streamlit as st
import json
import os

CHECKLIST_FILE = "checklist_reduction.json"

DEFAULT_PLAN = {
    "Marca": ["Criar logotipo", "Escolher cores"],
    "Produtos Iniciais": ["Piteiras de vidro", "Sedas", "Tesoura pequena", "Cuia"],
    "Drops": ["Definir frequência", "Definir quantidade por drop", "Planejar divulgação"],
    "Marketing": ["Criar Instagram", "Criar grupo WhatsApp", "Gerar conteúdo educativo"],
    "Embalagem": ["Definir embalagem", "Criar flyers informativos"],
    "Pagamento e Entrega": ["Definir métodos de pagamento", "Definir opções de entrega"],
    "Financeiro": ["Criar planilha de controle"]
}

def load_checklist():
    if os.path.exists(CHECKLIST_FILE):
        with open(CHECKLIST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {section: {item: False for item in items} for section, items in DEFAULT_PLAN.items()}

def save_checklist(checklist):
    with open(CHECKLIST_FILE, "w", encoding="utf-8") as f:
        json.dump(checklist, f, ensure_ascii=False, indent=4)

st.title("Reduction Planner ✅")

checklist = load_checklist()

for section, items in checklist.items():
    with st.expander(section):
        for item in items:
            checked = st.checkbox(item, value=items[item], key=f"{section}-{item}")
            checklist[section][item] = checked

if st.button("Salvar Progresso"):
    save_checklist(checklist)
    st.success("Checklist salvo com sucesso!")