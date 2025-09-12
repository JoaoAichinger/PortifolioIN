import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SearchWindow from './components/SearchWindow'
import MyHeader from './components/MyHeader'
import Introduction from './components/Introduction'

function App() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <MyHeader></MyHeader>
      <Introduction className="intro"></Introduction>
      <SearchWindow className="searchContainer"></SearchWindow>
      
    </>
  );
}

export default App;
