import { useState } from 'react'
import './App.css'
var result = true;
function App() {
  

  const flip = () =>{
    result=!result;
    console.log(`it entered{result}`)
  }
  return (
    <>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn testmore {result}
      </p>
    </>
  )
}

export default App
