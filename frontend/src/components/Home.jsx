import { useState } from 'react'
import SearchWindow from './SearchWindow'
import MyHeader from './MyHeader'
import Introduction from './Introduction'

function Home() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <MyHeader></MyHeader>
      <Introduction className="intro"></Introduction>
      <SearchWindow className="searchContainer"></SearchWindow>
      
    </>
  );
}

export default Home;
