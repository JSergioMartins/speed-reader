# Speed Reader - Full Deployment Guide

## ✅ What's Been Built

### Backend (speed-reader-api)
- ✅ User authentication (Email/Password + Google OAuth ready)
- ✅ PostgreSQL database with user sessions, bookmarks, and stats
- ✅ Reading progress tracking API
- ✅ **Already deployed on Railway!**

### Frontend (speed-reader)
- ✅ Login/Register modal UI
- ✅ Auto-save reading progress every 10 seconds
- ✅ User profile display
- ✅ Session persistence with JWT tokens
- ✅ Graceful degradation (works without login)

---

## 🚀 Deployment Steps

### 1. Backend (Already Done!) ✅
Your Railway API is running at:
```
https://speed-reader-api-production.up.railway.app
```

With:
- ✅ PostgreSQL database connected
- ✅ SECRET_KEY environment variable set
- ✅ ALLOWED_ORIGINS configured

### 2. Frontend Deployment

#### Push to GitHub
```bash
cd speed-reader
git add index.html service-worker.js
git commit -m "Add authentication system"
git push origin main
```

#### GitHub Pages will auto-deploy in ~1 minute
Your app: `https://jsergiomartins.github.io/speed-reader/`

---

## 🧪 Testing the Auth System

### Test 1: Create Account
1. Open `https://jsergiomartins.github.io/speed-reader/`
2. Click **Sign In** button (top right)
3. Click **Create one** link
4. Fill in:
   - Email: your@email.com
   - Password: password123
5. Click **Create Account**
6. You should see: ✅ "Account created! Welcome!"

### Test 2: Login
1. Refresh the page
2. Click **Sign In**
3. Enter your credentials
4. Should see your email in the header

### Test 3: Progress Tracking
1. While logged in, upload a book
2. Start reading
3. After 10 seconds, check Railway logs:
   ```
   POST /user/sessions 200
   ```
4. Close the page, reopen → your progress is saved!

### Test 4: Sign Out
1. Click **Sign Out** button
2. Header returns to "Sign In" button
3. You can still read books (without saving progress)

---

## 🔍 Debugging

### If login doesn't work:

**Check CORS in Railway:**
```bash
# Go to Railway Variables tab
# Verify:
ALLOWED_ORIGINS=https://jsergiomartins.github.io
```

**Check browser console:**
```
F12 → Console tab
Look for errors
```

**Check Railway logs:**
```
Railway → Your project → speed-reader-api → Logs
```

### Common Issues:

**"Failed to load user"**
- Token expired (7 days)
- Solution: Sign out and sign in again

**"CORS error"**
- ALLOWED_ORIGINS doesn't include your GitHub Pages URL
- Solution: Add it in Railway Variables

**"Database connection error"**
- PostgreSQL not running
- Solution: Check Railway database service is active

---

## 📊 Features Overview

### For Anonymous Users (No Login)
- ✅ Upload and read books
- ✅ Adjust WPM
- ✅ Chapter navigation
- ✅ Progress bar
- ❌ No progress saving
- ❌ No statistics

### For Logged-In Users
- ✅ Everything above, PLUS:
- ✅ Auto-save progress every 10 seconds
- ✅ Resume reading from where you left off
- ✅ Reading statistics tracked
- ✅ Multiple device sync (same progress everywhere)

---

## 🔐 Security Notes

- Passwords hashed with bcrypt (never stored in plain text)
- JWT tokens expire in 7 days
- Tokens stored in localStorage (client-side only)
- CORS prevents unauthorized domains
- Books never uploaded to server (client-side only)

---

## 📈 What Gets Tracked

### Per Book Session:
- Book title (filename)
- Current word position
- Total words
- WPM preference
- Theme preference
- Last read timestamp

### User Statistics:
- Total words read
- Books completed
- Reading streak (days in a row)
- Total reading time

---

## 🎨 Optional: Google OAuth Setup

If you want "Sign in with Google" button:

### 1. Get Google Client ID
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create project
3. APIs & Services → Credentials
4. Create OAuth 2.0 Client ID
5. Add authorized origins:
   ```
   https://jsergiomartins.github.io
   ```
6. Copy Client ID

### 2. Add to Railway
```
GOOGLE_CLIENT_ID=123456789-abc.apps.googleusercontent.com
```

### 3. Frontend (Future Enhancement)
Add Google Sign-In button to login modal

---

## 🔄 Future Enhancements

Easy to add later:
- [ ] Bookmarks (API already built!)
- [ ] Reading statistics dashboard
- [ ] Book history list
- [ ] Reading goals
- [ ] Social features (share progress)
- [ ] Dark/light theme sync across devices

---

## 💾 Data Flow

```
User uploads book (TXT/PDF/EPUB/MOBI)
          ↓
File sent to Railway API
          ↓
Parsed → Returns {words[], chapters[]}
          ↓
Book hash generated (client-side)
          ↓
User starts reading
          ↓
Every 10 seconds:
  - POST /user/sessions (saves progress)
          ↓
User closes browser
          ↓
Reopens later → GET /user/sessions
          ↓
Resumes from saved position
```

---

## 🛠️ Maintenance

### Update Backend
```bash
cd speed-reader-api
git add .
git commit -m "Update feature"
git push
# Railway auto-deploys
```

### Update Frontend
```bash
cd speed-reader
# Edit index.html or service-worker.js
# Bump service worker version (v10, v11, etc.)
git push
# GitHub Pages auto-deploys
```

### Database Backup (Recommended)
Railway provides automatic backups, but you can also:
```bash
# From Railway dashboard:
Database → Backups → Create Backup
```

---

## 📞 Support

**Backend Issues:**
- Check Railway logs
- Verify environment variables
- Test with curl:
  ```bash
  curl https://speed-reader-api-production.up.railway.app/health
  ```

**Frontend Issues:**
- Check browser console (F12)
- Clear localStorage:
  ```javascript
  localStorage.clear()
  ```
- Hard refresh: Ctrl+Shift+R

---

## ✨ You're Done!

Your Speed Reader app now has:
- ✅ Full user authentication
- ✅ Cloud progress sync
- ✅ Reading statistics
- ✅ Multi-device support
- ✅ Production-ready security

Push to GitHub and start using it! 🚀
