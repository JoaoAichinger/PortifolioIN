import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SearchWindow from './components/SearchWindow'
import MyHeader from './components/MyHeader'

function App() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <header>
        <MyHeader></MyHeader>
      </header>
      
      <SearchWindow></SearchWindow>
      
    </>
  );
}

export default App;
