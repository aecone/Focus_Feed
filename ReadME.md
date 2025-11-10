
# 🧘‍♀️ Focus Feed

**Focus Feed** is a distraction-free social media viewer designed to help users stay informed without falling into the endless scroll.  
Instead of wading through ads, recommended posts, and cluttered interfaces, users can view only the updates they care about — cleanly, calmly, and without distractions.

👩‍🏫 **Built as part of:** *Girls Who Code’s Leadership Academy Program*

🌐 **Live Site:** [focus-feed-iota.vercel.app](https://focus-feed-iota.vercel.app/#)  
🎨 **Figma Design:** [View on Figma](https://www.figma.com/design/vRbHIWC0sdYglCVzMHsJ21/Feed?node-id=0-1&t=piou6JrDiluM9LR7-1)

> ⚠️ **Note:** The site’s Instagram scraping functionality is currently **inactive** — our Scrapfly API ran out of credits 😅.  
> The frontend and backend are still fully deployable and functional locally.

<table style="border: none; border-collapse: collapse;">
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/a61ef495-02be-4316-ae21-59a4acf48efa" width="300" />
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/454ed849-e7b7-4134-a7c6-b7449130e517" width="300" /><br>
      <img src="https://github.com/user-attachments/assets/f364c4a8-6a9e-4410-8b35-1c91aaf74ad9" width="300" />
    </td>
  </tr>
</table>



---

## 🚀 Tech Stack

### **Frontend**
- [React](https://react.dev/)  

### **Backend**
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Scrapfly](https://scrapfly.io/) for web scraping (paid API)
- [Supabase](https://supabase.com/) for hosted PostgreSQL database

### **Deployment**
- **Frontend:** [Vercel](https://vercel.com/)
- **Backend:** [Render](https://render.com/)

---

## ⚙️ Setup Instructions

### 1. **Backend Setup**
```bash
cd backend
pip install -r requirements.txt
````

* Make sure to set up **database credentials** locally before running.

Run the backend:

```bash
flask --app app/app.py run --debug
```

### 2. **Frontend Setup**

```bash
cd frontend
npm install
npm start
```

The React frontend will launch on `localhost:3000`
Make sure the backend is running in another terminal window.

---

## 🧩 Features

### **MVP**

* Fetch and display public Instagram posts in a clean, unified feed
* User authentication and personalized feeds
* Search bar for finding accounts/posts
* Dark and light mode

---

## 👩‍💻 Team

| Name                                                 | Role                |
| ---------------------------------------------------- | ------------------- |
| [Anna Belenko](https://github.com/annabelenko)       | Front-End Developer |
| [Rocio Vasquez](https://github.com/RocioJV)     | Front-End Developer |
| [Andrea](https://github.com/aecone)                | Back-End Developer  |
| [Aneesha Acharya](https://github.com/aneeshaa1) | Back-End Developer  |

---
