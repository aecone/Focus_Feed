import React, { useState, useEffect } from 'react';
import './Feed.css';
import FeedPost from '../FeedPost/FeedPost';

function Feed() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    // Fetch posts from your backend
    fetch('http://127.0.0.1:5000/posts/rutgerswics')
      .then(response => response.json())
      .then(data => setPosts(data.posts))
      .catch(error => console.error('Error fetching posts:', error));
  }, []);

  return (
    <section className="feed-grid">
      {posts.map((post, index) => (
        <FeedPost
          key={post.post_id}
          src={post.src}
          caption={post.caption_text}
          link={post.link}
        />
      ))}
    </section>
  );
}

export default Feed;
