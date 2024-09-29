CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  pw VARCHAR(100) NOT NULL
);

CREATE TABLE insta_accounts (
  insta_account_id SERIAL PRIMARY KEY,
  insta_username VARCHAR(100) NOT NULL
);

CREATE TABLE posts (
  post_id SERIAL PRIMARY KEY,
  insta_account_id INT REFERENCES insta_accounts(insta_account_id),
  post_id_str VARCHAR(20) NOT NULL,         -- Corresponds to "id"
  shortcode VARCHAR(20) NOT NULL,            -- Corresponds to "shortcode"
  dimensions_height INT NOT NULL,            -- Corresponds to "dimensions.height"
  dimensions_width INT NOT NULL,             -- Corresponds to "dimensions.width"
  src TEXT NOT NULL,                         -- Corresponds to "src"
  src_attached TEXT,                         -- Corresponds to "src_attached"
  video_url TEXT,                           -- Corresponds to "video_url"
  location TEXT,                            -- Corresponds to "location"
  taken_at TIMESTAMP NOT NULL,              -- Corresponds to "taken_at"
  is_video BOOLEAN NOT NULL,                 -- Corresponds to "is_video"
  link TEXT NOT NULL,                         -- Corresponds to "link"
  caption_text TEXT NOT NULL                 -- Corresponds to "captions"
);


CREATE TABLE subscriptions (
  subscription_id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(user_id),
  insta_account_id INT REFERENCES insta_accounts(insta_account_id)
);
