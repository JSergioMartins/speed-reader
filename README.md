# Speed Reader - PWA Speed Reading App

Train your brain to read at lightning speed! 📖⚡

## Features

- 📚 Support for TXT and PDF files
- ⚡ Adjustable reading speed (100-1000 WPM)
- 📱 Progressive Web App (works offline)
- 🎯 Clean, distraction-free reading experience
- ⌨️ Keyboard shortcuts (Space to play/pause, arrows to skip)

## Deploy to GitHub Pages

### Step 1: Create a GitHub Account
If you don't have one, go to [github.com](https://github.com) and sign up.

### Step 2: Create a New Repository
1. Click the **+** icon in the top right → **New repository**
2. Name it: `speed-reader` (or any name you like)
3. Make it **Public**
4. **DO NOT** check "Initialize with README"
5. Click **Create repository**

### Step 3: Upload Files
You have two options:

#### Option A: Using GitHub Web Interface (Easiest)
1. On your new repository page, click **uploading an existing file**
2. Drag and drop these files:
   - `index.html`
   - `manifest.json`
   - `service-worker.js`
   - `icon-192.png` (create this first - see below)
   - `icon-512.png` (create this first - see below)
3. Click **Commit changes**

#### Option B: Using Git Command Line
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR-USERNAME/speed-reader.git
git branch -M main
git push -u origin main
```

### Step 4: Enable GitHub Pages
1. Go to your repository **Settings**
2. Click **Pages** in the left sidebar
3. Under **Source**, select **main** branch
4. Click **Save**
5. Wait 1-2 minutes

Your app will be live at:
```
https://YOUR-USERNAME.github.io/speed-reader/
```

## Creating App Icons

### Quick Method (Placeholder Icons):
1. Open `create-icons.html` in your browser
2. It will automatically download `icon-192.png` and `icon-512.png`
3. Upload these to your repository

### Better Method (Custom Icons):
1. Create a 512x512 PNG image with your design
2. Use a tool like [RealFaviconGenerator](https://realfavicongenerator.net/) to create all sizes
3. Replace `icon-192.png` and `icon-512.png` with your versions

## Installing as PWA

### On iOS (iPhone/iPad):
1. Open your deployed site in **Safari**
2. Tap the **Share** button
3. Scroll down and tap **Add to Home Screen**
4. Tap **Add**

### On Android:
1. Open your deployed site in **Chrome**
2. Tap the **three dots** menu
3. Tap **Install app** or **Add to Home Screen**

### On Desktop (Chrome/Edge):
1. Look for the **install icon** in the address bar
2. Click it and confirm
3. The app will open in its own window

## Updating Your App

Just edit the files and commit changes to GitHub. Updates will be live in 1-2 minutes!

To force users to get the new version, increment the version number in `service-worker.js`:
```javascript
const CACHE_NAME = 'speed-reader-v2'; // Change v1 to v2, v3, etc.
```

## Customization

### Change Colors:
Edit the CSS variables in `index.html`:
```css
:root {
    --bg-dark: #0a0e1a;
    --accent: #00ff9d;
    /* etc. */
}
```

### Change Reading Speed Range:
```html
<input type="range" min="100" max="2000" value="300">
```

## Support

- Works on iOS 11.3+ (Safari)
- Works on Android 5+ (Chrome)
- Works on desktop browsers

## License

Free to use and modify!

---

Built with ❤️ for speed readers everywhere
