# Deploy Agri Mitra

## Option 1: Replit (Easiest – No Git Required)

1. **Go to [replit.com](https://replit.com)** and sign in.

2. **Create new Repl** → Click **"Create Repl"** → Choose **"Import from GitHub"**  
   - If you don't have a GitHub repo yet: choose **"Upload project"** instead, zip your `frontend` folder, and upload it.

3. **If using GitHub first:**
   - Create a repo at [github.com/new](https://github.com/new) (e.g. `agri-mitra`).
   - Install [Git](https://git-scm.com) if needed, then in a terminal:
     ```bash
     cd path/to/frontend
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/agri-mitra.git
     git push -u origin main
     ```
   - In Replit: **Import from GitHub** → select your repo.

4. **Set Secrets** (Environment Variables):  
   In Replit: **Tools** → **Secrets** → Add:
   - `MYSQL_HOST` – your MySQL host
   - `MYSQL_USER` – MySQL user
   - `MYSQL_PASSWORD` – MySQL password
   - `MYSQL_DATABASE` = `agri_mitra`
   - `SECRET_KEY` – any random string
   - `OTP_DEMO` = `1234`
   - `OPENAI_API_KEY` – optional, for AI features

5. **Run** – Replit uses `.replit` to run:
   ```
   cd backend && pip install -r requirements.txt && python app.py
   ```

6. **Deploy** – Click **Deploy** → Your app will be live at `https://your-repl-name.username.repl.co`.

---

## Option 2: Render.com

1. **Push to GitHub** (see step 3 above if needed).

2. **Go to [render.com](https://render.com)** and sign in with GitHub.

3. **New** → **Web Service** → Connect your GitHub repo.

4. **Settings:**
   - **Build command:** `pip install -r backend/requirements.txt`
   - **Start command:** `cd backend && gunicorn -w 1 -b 0.0.0.0:$PORT app:app`
   - **Environment:** Add `MYSQL_*`, `SECRET_KEY`, `OTP_DEMO`, etc. (same as Replit).

5. **Deploy** – Render builds and deploys. You get a URL like `https://agri-mitra.onrender.com`.

---

## Option 3: Railway

1. **Push to GitHub** (see step 3 above).

2. **Go to [railway.app](https://railway.app)** → **Start a New Project** → **Deploy from GitHub repo**.

3. **Add MySQL** – Railway → **New** → **Database** → **MySQL**. Note the `MYSQL_*` values.

4. **Variables** – Add `MYSQL_*`, `SECRET_KEY`, `OTP_DEMO`, `OPENAI_API_KEY` to your service.

5. **Deploy** – Railway auto-deploys from GitHub.

---

## MySQL Options (if you don't have one)

- **[PlanetScale](https://planetscale.com)** – Free MySQL (needs a few tweaks for compatibility).
- **[Railway MySQL](https://railway.app)** – Add MySQL from dashboard.
- **Replit** – Use Replit Database or an external MySQL URL.
- **Local** – For local dev only: `localhost` with your own MySQL.

---

## After Deployment

- **Frontend URL:** Your deployed URL (e.g. `https://xxx.replit.app` or `https://xxx.onrender.com`).
- **API base:** Same origin – `config.js` uses the current host when not on `localhost`.
- **Test:** Register with any 10-digit phone, OTP `1234`, then open Profile and AI Assistant.
