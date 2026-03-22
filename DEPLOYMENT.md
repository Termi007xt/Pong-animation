# Vercel Deployment Guide

## Prerequisites

1. GitHub account
2. Vercel account (sign up at https://vercel.com)
3. Git installed on your machine

## Deployment Steps

### Step 1: Prepare Your Project

Ensure you have these files in your project directory:
- `app.py`
- `index.html`
- `ascii_dictionary.py`
- `Dynamic_loader_ascii.py`
- `vercel.json`
- `requirements.txt`
- `.gitignore`

### Step 2: Initialize Git Repository

Open terminal in your project directory and run:

```bash
cd "PONG Animation"
git init
git add .
git commit -m "Initial commit"
```

### Step 3: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., "pong-animation-generator")
3. Do NOT initialize with README, .gitignore, or license
4. Copy the repository URL

### Step 4: Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual values.

### Step 5: Deploy to Vercel

#### Option A: Using Vercel Dashboard (Recommended)

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration
5. Click "Deploy"
6. Wait for deployment to complete (1-2 minutes)
7. Your app will be live at: `https://your-project-name.vercel.app`

#### Option B: Using Vercel CLI

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

4. Follow the prompts and confirm deployment

### Step 6: Access Your Application

Once deployed, Vercel will provide a URL like:
```
https://pong-animation-generator.vercel.app
```

Visit this URL to use your application.

## Configuration Files Explained

### vercel.json
Tells Vercel how to build and route your Flask application.

### requirements.txt
Lists Python dependencies that Vercel will install.

### .gitignore
Prevents unnecessary files from being committed to Git.

## Updating Your Deployment

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

Vercel will automatically redeploy your application.

## Custom Domain (Optional)

1. Go to your project in Vercel Dashboard
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Troubleshooting

### Build Fails
- Check that all files are committed to Git
- Verify `requirements.txt` has correct dependencies
- Check Vercel build logs for specific errors

### Application Not Loading
- Ensure `vercel.json` is properly configured
- Check that `app.py` has the correct Flask app structure
- Verify all imports are available in `requirements.txt`

### 404 Errors
- Ensure routes in `vercel.json` are correct
- Check that `index.html` is in the root directory

## Environment Variables (If Needed)

If you need to add environment variables:

1. Go to Vercel Dashboard → Your Project
2. Click "Settings" → "Environment Variables"
3. Add your variables
4. Redeploy the application

## Support

For Vercel-specific issues, visit:
- Documentation: https://vercel.com/docs
- Support: https://vercel.com/support
