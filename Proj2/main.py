from src.data_loader import load_data
from src.preprocessing import encode_target, encode_categoricals, normalize_data
from src.model_selection import get_best_models
from sklearn.model_selection import train_test_split
from src.model_selection import evaluate_models

# 1. Carregar dados
df = load_data('data.csv')

# 2. Pré-processamento
df = encode_target(df)
df = encode_categoricals(df)
# 3. Separar features (X) e target (y)

X = df.drop('Target', axis=1)
y = df['Target']
df = normalize_data(df)


print(y.unique())
print(y.dtype)

# 4. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Verificar um pedaço do X_train (opcional)
print(X_train.head())


models = get_best_models(X_train, y_train)
for name, model in models.items():
    print(f"{name}: best params -> {model.best_params_}")

evaluate_models(models, X_test, y_test)
