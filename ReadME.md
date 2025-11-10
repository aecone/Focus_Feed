
# 🧘‍♀️ Focus Feed

**Focus Feed** is a distraction-free social media viewer designed to help users stay informed without falling into the endless scroll.  
Instead of wading through ads, recommended posts, and cluttered interfaces, users can view only the updates they care about — cleanly, calmly, and without distractions.

👩‍🏫 **Built as part of:** *Girls Who Code’s Leadership Academy Program*

🌐 **Live Site:** [focus-feed-iota.vercel.app](https://focus-feed-iota.vercel.app/#)  
🎨 **Figma Design:** [View on Figma](https://www.figma.com/design/vRbHIWC0sdYglCVzMHsJ21/Feed?node-id=0-1&t=piou6JrDiluM9LR7-1)

> ⚠️ **Note:** The site’s Instagram scraping functionality is currently **inactive** — our Scrapfly API ran out of credits 😅.  
> The frontend and backend are still fully deployable and functional locally.

<table>
  <tr>
    <td>
      <img width="300" alt="Screenshot 2025-11-10 at 6 04 44 PM-min" src="https://github.com/user-attachments/assets/95abb1f2-8323-4aef-9b2a-a248746e7b76" />
    </td>
    <td>
      <img width="300" alt="Screenshot_2024-11-11_at_2 26 03_AM-min" src="https://github.com/user-attachments/assets/d7f085c4-1ee1-4278-ba39-fbeb44a0d8ed" /><br>
      <img width="300" alt="Screenshot 2025-11-10 at 6 05 07 PM-min" src="https://github.com/user-attachments/assets/2cb94cab-db92-44d8-93d3-d5d1a07b6d7e" />
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
