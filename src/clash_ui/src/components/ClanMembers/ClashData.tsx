import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface DataItem {
  message: Blob
  // Define other properties as needed
}
const base_url = 'http://localhost:5000'

function DataDisplay() {
  const [userData, setUserData] = useState<DataItem[]>([]);
  const getClanMembers = async () => {
      const response = await axios.get(`${base_url}/clan-members`);
      setUserData(response.data);
    };

    useEffect(() => {
        getClanMembers();
    }, []);
//   useEffect(() => {
//     // Replace 'API_ENDPOINT' with the actual API endpoint you want to fetch data from
//     axios.get<DataItem[]>('http://localhost:5000/clan-members')
//       .then((response:any) => {
//         setData(response.data);
//         setLoading(false);
//       })
//       .catch((error:any) => {
//         console.error('Error fetching data:', error);
//         setLoading(fals  e);
//       });
//   }, []);

//   if (loading) {
//     return <div>Loading...</div>;
//   }

  return (

    <div className="App">
    <header className="App-header">
      <h2>GitHub User Data</h2>
    </header>
  </div>    // <div>
    //   <h1>Data Display</h1>
    //   <ul>
    //     {/* {userData} */}
    //     {/* {userData.map(item => (
    //       <li key={item.id}>{item.name}</li>
    //     ))} */}
    //   </ul>
    // </div>
  );
}

export default DataDisplay;