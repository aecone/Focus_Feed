import React, { useState } from 'react';
import './FeedPost.css';

function FeedPost({ src, caption, link }) {
  const [isExpanded, setIsExpanded] = useState(false);

  const proxySrc = `http://127.0.0.1:5000/proxy-image?url=${encodeURIComponent(src)}`;

  const toggleExpand = (event) => {
    event.stopPropagation();
    setIsExpanded(!isExpanded);
  };

  return (
    <div className={`card ${isExpanded ? 'expanded' : ''}`}>
      {/* Image */}
      <a href={link} target="_blank" rel="noopener noreferrer">
        <img src={proxySrc} alt={caption} className="post-image" />
      </a>

      {/* MORE/LESS button */}
      {!isExpanded && (
        <button className="toggle-button" onClick={toggleExpand}>
          MORE
        </button>
      )}
      {isExpanded && (
        <button className="toggle-button" onClick={toggleExpand}>
          LESS
        </button>
      )}
       {/* Caption */}
       <p className="post-caption">{caption}</p>
    </div>
  );
}

export default FeedPost;
