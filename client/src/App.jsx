import React from 'react'
import { BrowserRouter,Routes,Route } from 'react-router-dom'
import GetEvent from './pages/GetEvent.jsx'

export default function App() {
  return (
  <BrowserRouter>
      <Routes>
     <Route path='/' element={<GetEvent/>}/>
    
      </Routes>
    </BrowserRouter>
  )
}
