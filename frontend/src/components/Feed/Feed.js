import React, { useState, useEffect } from "react";
import "./Feed.css";
import FeedPost from "../FeedPost/FeedPost";

function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log("API Base URL:", process.env.REACT_APP_API_BASE_URL);

    fetch(`${process.env.REACT_APP_API_BASE_URL}/posts/rutgerswics`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setPosts(data.posts);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching posts:", error);
        setLoading(false);
      });
  }, []);

  return (
    <section className="feed-grid">
      {loading ? (
        <p>Loading...</p>
      ) : (
        posts.map((post, index) => (
          <FeedPost
            key={post.post_id}
            src={post.src}
            caption={post.caption_text}
            link={post.link}
          />
        ))
      )}
    </section>
  );
}

export default Feed;
