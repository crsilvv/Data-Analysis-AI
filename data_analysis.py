import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Importar a planilha
file_path = "gym_members_exercise_tracking.xlsx"
df = pd.read_excel(file_path)

# Ajustar estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Distribuição por Gênero
gender_counts = df["Gender"].value_counts()

plt.figure()
sns.countplot(data=df, x="Gender", palette="pastel")
plt.title("Distribuição por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Número de Membros")
plt.tight_layout()
plt.savefig("grafico_genero.png")

# Altura vs Peso com tamanho por frequência
plt.figure()
scatter = sns.scatterplot(
    data=df,
    x="Height (m)",
    y="Weight (kg)",
    hue="Workout_Frequency (days/week)",
    size="Workout_Frequency (days/week)",
    palette="viridis",
    sizes=(20, 200),
    legend="brief"
)
plt.title("Peso vs Altura (com Frequência de Treino)")
plt.tight_layout()
plt.savefig("grafico_peso_altura_frequencia.png")

# Idade vs Frequência de Treino
plt.figure()
sns.scatterplot(data=df, x="Age", y="Workout_Frequency (days/week)", hue="Gender", palette="Set2")
plt.title("Idade vs Frequência de Treino")
plt.tight_layout()
plt.savefig("grafico_idade_frequencia.png")

# Atividades mais praticadas
plt.figure()
sns.countplot(data=df, x="Workout_Type", order=df["Workout_Type"].value_counts().index, palette="Set3")
plt.title("Atividades Mais Praticadas")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafico_atividades.png")

# Calorias vs Idade por Atividade
grouped = df.groupby("Workout_Type").agg({"Calories_Burned": "mean", "Age": "mean"}).reset_index()

plt.figure()
sns.barplot(data=grouped, x="Workout_Type", y="Calories_Burned", palette="coolwarm")
plt.title("Média de Calorias Queimadas por Tipo de Atividade")
plt.ylabel("Calorias Queimadas")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafico_calorias_atividade.png")

# Exibir os arquivos gerados
file_paths = {
    "Distribuição por Gênero": "grafico_genero.png",
    "Peso vs Altura vs Frequência": "grafico_peso_altura_frequencia.png",
    "Idade vs Frequência de Treino": "grafico_idade_frequencia.png",
    "Atividades Mais Praticadas": "grafico_atividades.png",
    "Calorias vs Tipo de Atividade": "grafico_calorias_atividade.png",
}

file_paths
