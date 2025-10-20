import pandas as pd, csv, sys, os, tempfile, shutil

def detect_sep(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        sample = f.read(8192)
    try:
        return csv.Sniffer().sniff(sample).delimiter
    except Exception:
        for s in ['\t', ';', ',']:
            if s in sample:
                return s
    return ','

PATH = "marketing_campaign.csv"
SEP = detect_sep(PATH)
try:
    df = pd.read_csv(PATH, sep=SEP, engine='c')
except FileNotFoundError:
    print("ERROR: File not found:", PATH)
    sys.exit(1)

print("INITIAL SHAPE:", df.shape)
print("\nMissing values per column (before):")
print(df.isnull().sum().sort_values(ascending=False).to_string())

print("\nDuplicate rows (before):", df.duplicated().sum())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=False).str.replace('-', '_', regex=False)
rows_before = df.shape[0]
df = df.drop_duplicates()
print("Duplicate rows removed:", rows_before - df.shape[0])

if 'income' in df.columns:
    df['income'] = df['income'].astype(str).str.replace('[^0-9.]', '', regex=True).replace('', pd.NA)
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    median_income = df['income'].median()
    # avoid inplace chained assignment warning:
    df['income'] = df['income'].fillna(median_income)
    print("✅ Income filled with median:", median_income)

obj_cols = df.select_dtypes(include='object').columns.tolist()
if obj_cols:
    df[obj_cols] = df[obj_cols].fillna('Unknown')
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip().str.title()

if 'education' in df.columns:
    df['education'] = df['education'].replace({
        'Phd': 'PhD', '2n Cycle': '2nd Cycle', '2n cycle': '2nd Cycle', '2N Cycle': '2nd Cycle',
        'Master': "Master's", 'Graduation': 'Graduate', 'Basic': 'Basic'
    })

if 'marital_status' in df.columns:
    df['marital_status'] = df['marital_status'].replace({
        'Alone': 'Single', 'Together': 'Married', 'Absurd': 'Unknown', 'Widow': 'Widowed'
    })

if 'gender' in df.columns:
    df['gender'] = df['gender'].replace({'M': 'Male', 'F': 'Female'}).str.title()

if 'country' in df.columns:
    df['country'] = df['country'].replace({'Usa': 'USA', 'U.s.a.': 'USA', 'United States': 'USA'}).str.title()

date_cols = [c for c in df.columns if 'dt_' in c or 'date' in c.lower()]
for c in date_cols:
    df[c] = pd.to_datetime(df[c], errors='coerce', dayfirst=True)
    try:
        df[c] = df[c].dt.strftime('%d-%m-%Y')
    except Exception:
        pass

if 'year_birth' in df.columns:
    df['age'] = 2025 - pd.to_numeric(df['year_birth'], errors='coerce')
    df.loc[(df['age'] < 15) | (df['age'] > 100), 'age'] = pd.NA
    df['age'] = df['age'].astype('Int64')
    print("✅ Age column created and cleaned.")

num_cols = [
    'recency','mntwines','mntfruits','mntmeatproducts','mntfishproducts',
    'mntsweetproducts','mntgoldprods','numdealspurchases','numwebpurchases',
    'numcatalogpurchases','numstorepurchases','numwebvisitsmonth','z_costcontact','z_revenue'
]
for n in num_cols:
    if n in df.columns:
        df[n] = pd.to_numeric(df[n], errors='coerce').fillna(0)

print("\nMissing values per column (after):")
print(df.isnull().sum().sort_values(ascending=False).to_string())

OUT_BASE = "marketing_campaign_cleaned.csv"
OUT_FALLBACK = "marketing_campaign_cleaned_v2.csv"

def safe_write(df, out_path, fallback):
    # write to a temp file then move to out_path
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".csv", dir=".")
    os.close(tmp_fd)
    try:
        df.to_csv(tmp_path, index=False)
        try:
            # attempt atomic replace
            shutil.move(tmp_path, out_path)
            return out_path
        except PermissionError:
            # fallback: try fallback filename
            shutil.move(tmp_path, fallback)
            return fallback
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise e

try:
    saved = safe_write(df, OUT_BASE, OUT_FALLBACK)
    print("\n🎯 Final shape:", df.shape)
    print("✅ Cleaned file saved as:", saved)
except Exception as e:
    print("ERROR while saving cleaned file:", str(e))
    print("Try closing the file if it's open in Excel/OneDrive, or delete the existing file and re-run.")
    sys.exit(1)

print("\nSample rows:")
print(df.head(10).to_string(index=False))
