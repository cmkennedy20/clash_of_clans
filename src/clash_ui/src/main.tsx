import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import ClashData from './ClashData.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <ClashData/>
  </React.StrictMode>,
)
