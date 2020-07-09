import React from 'react';
import './App.css';
import {FeedsApi} from './api';

function App() {
    const feedsApi = new FeedsApi();
    feedsApi.feedsGet({}).then(feeds => {
        console.log(feeds);
    });
    return (
    <div className="App">
      <header className="App-header">
      	Feeds may be found in the console
      </header>
    </div>
  );
}

export default App;
