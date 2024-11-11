-- Drop tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS insta_accounts;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  pw TEXT NOT NULL,
  update_frequency INT DEFAULT 3
);

-- Create insta_accounts table
CREATE TABLE insta_accounts (
    insta_account_id BIGINT PRIMARY KEY,
      insta_username TEXT UNIQUE NOT NULL
);

-- Create posts table
CREATE TABLE posts (
  post_id SERIAL PRIMARY KEY,
  insta_account_id BIGINT REFERENCES insta_accounts(insta_account_id),
  post_id_str TEXT NOT NULL,           -- Corresponds to "id"
  shortcode TEXT NOT NULL,             -- Corresponds to "shortcode"
  dimensions_height INT NOT NULL,      -- Corresponds to "dimensions.height"
  dimensions_width INT NOT NULL,       -- Corresponds to "dimensions.width"
  src TEXT NOT NULL,                   -- Corresponds to "src"
  src_attached TEXT,                   -- Corresponds to "src_attached"
  video_url TEXT,                      -- Corresponds to "video_url"
  location TEXT,                       -- Corresponds to "location"
  taken_at TIMESTAMP NOT NULL,         -- Corresponds to "taken_at"
  is_video BOOLEAN NOT NULL,           -- Corresponds to "is_video"
  link TEXT NOT NULL,                  -- Corresponds to "link"
  caption_text TEXT NOT NULL           -- Corresponds to "captions"
);

-- Create subscriptions table
CREATE TABLE subscriptions (
  subscription_id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(user_id),
  insta_account_id BIGINT REFERENCES insta_accounts(insta_account_id)
);
