import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface DataItem {
  id: number;
  name: string;
  // Define other properties as needed
}

function DataDisplay() {
  const [data, setData] = useState<DataItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Replace 'API_ENDPOINT' with the actual API endpoint you want to fetch data from
    axios.get<DataItem[]>('API_ENDPOINT')
      .then((response:any) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error:any) => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Data Display</h1>
      <ul>
        {data.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default DataDisplay;