import React from 'react';
import './Feed.css';
import FeedPost from '../FeedPost/FeedPost';

function Feed() {
  return (
    <section className="feed-grid">
      {[...Array(8)].map((_, index) => (
        <FeedPost key={index} />
      ))}
    </section>
  );
}

export default Feed;