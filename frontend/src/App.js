import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div>
      {/* <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div> */}

    <div>
      <body>
          {/* contains the navbar */}
          <header>
              <div class="logo">FocusFeed</div>
              <div class = "navbar">
                  
                  <nav>
                      <ul>
                          {/* list items for each section: Feed, Follow, and Profile */}
                          <li><a href="#">Feed</a></li>
                          <li><a href="#">Follow</a></li>
                          <li><a href="#">Profile</a></li>
                      </ul>
                  </nav>
              </div>
          </header>

          {/* search bar section below the nav bar */}
          <div class = "search-bar">
              {/* input field for search queries */}
              <input type="text" placeholder="Search"/>
          </div>

          {/* grid container for the feed's content */}
          <main>
              <section class = "feed-grid">
                  {/* placeholder card for each post */}
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
                  <div class = "card"></div>
              </section>
          </main>
      </body>
      
    </div>
    </div>
  );
}

export default App;
