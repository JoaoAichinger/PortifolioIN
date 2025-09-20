import './MyFooter.css'

function MyFooter(){
    return(
        <footer className="footer">
      <div className="footer-container">
        
        {/* Coluna 1: Logo + descrição */}
        <div className="footer-column">
          <img 
            src="https://webapp377823.ip-23-239-29-170.cloudezapp.io/wp-content/uploads/2018/02/logo-visual-footer-300x213.png" 
            alt="Logo" 
            width="140" 
            height="105"
          />
          <p>
            Somos uma escola com metodologia americana, 100% presencial e prática, voltada à capacitação 
            para o mercado de trabalho nas áreas criativas e de inovação.
          </p>
        </div>

        {/* Coluna 2: Cursos */}
        <div className="footer-column">
          <h6>Nossos Cursos</h6>
          <ul>
            <li><a href="https://infinityschool.com.br/cursos/full-stack/">Curso Programação Full Stack IA</a></li>
            <li><a href="https://infinityschool.com.br/cursos/marketing-digital">Curso Marketing Digital IA</a></li>
            <li><a href="https://infinityschool.com.br/cursos/digital-design">Curso Design Full Stack IA</a></li>
            <li><a href="https://infinityschool.com.br/cursos/fotografia-design/">Curso Fotografia Design</a></li>
            <li><a href="https://infinityschool.com.br/cursos/data-science/">Curso Data Science</a></li>
            <li><a href="https://infinityschool.com.br/cursos/film-design/">Curso Film Design</a></li>
            <li><a href="https://infinityschool.com.br/cursos/kids">Curso Kids</a></li>
          </ul>
        </div>

        {/* Coluna 3: Unidades */}
        <div className="footer-column">
          <h6>Nossas Unidades</h6>
          <p><strong>SALVADOR</strong><br/>TEL: <a href="tel:08001800001">0800 180 0001</a><br/>Alameda Salvador, 1057, Edf. Salvador Shopping Business, Torre Europa, Sala 310</p>
          <p><strong>FORTALEZA</strong><br/>TEL: <a href="tel:08001800001">0800 180 0001</a><br/>Avenida Santos Dumont, Aldeota</p>
        </div>

        {/* Coluna 4: Mais unidades + Política de Privacidade */}
        <div className="footer-column">
          <p><strong>BELO HORIZONTE</strong><br/>TEL: <a href="tel:08001800001">0800 180 0001</a><br/>Avenida do Contorno, 6480, Loja 01, Savassi</p>
          <p><strong>RECIFE</strong><br/>TEL: <a href="tel:08001800001">0800 180 0001</a><br/>Avenida República do Líbano, 256 – Pina</p>
          <p><strong>SÃO PAULO</strong><br/>TEL: <a href="tel:08001800001">0800 180 0001</a><br/>Avenida Paulista, 777, Edf. Viking, Sala 12</p>
          <p><a href="https://webapp377823.ip-23-239-29-170.cloudezapp.io/politica-de-privacidade/">Política de Privacidade</a></p>
        </div>

      </div>
      <div className='botCopy'><p>© 2025 Infinity. Todos os direitos reservados.</p></div>
    </footer>
    );
}

export default MyFooter;