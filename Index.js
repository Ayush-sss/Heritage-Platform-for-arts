import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [talents, setTalents] = useState([]);
  const [destinations, setDestinations] = useState([]);

  useEffect(() => {
    // Retrieve list of talents and destinations from API
    axios.get('/talents')
      .then(response => setTalents(response.data.talents))
      .catch(error => console.log(error));

    axios.get('/destinations')
      .then(response => setDestinations(response.data.destinations))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Cultural Destination Platform</h1>
      <h2>Talents</h2>
      <ul>
        {talents.map(talent => (
          <li key={talent.id}>{talent.name}</li>
        ))}
      </ul>
      <h2>Destinations</h2>
      <ul>
        {destinations.map(destination => (
          <li key={destination.id}>{destination.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
