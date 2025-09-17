import { useState } from 'react'
import SearchWindow from './SearchWindow'
import MyHeader from './MyHeader'
import Introduction from './Introduction'
import  MyFooter from './MyFooter'
import AlunoList from './AlunoList';
import alunos from "../data/alunos.json"
function Home() {
  //const [count, setCount] = useState(0)

  return (
    <>
      <MyHeader></MyHeader>
      <Introduction className="intro"></Introduction>
      <SearchWindow className="searchContainer"></SearchWindow>
      <AlunoList alunos={alunos}></AlunoList>
      <MyFooter></MyFooter>
    </>
  );
}

export default Home;
