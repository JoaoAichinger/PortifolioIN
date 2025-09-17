import "./MyHeader.css"
import logo from "../assets/logo.png"

function MyHeader(){
    return(
        <header>
            <div className="center">
                <a href="https://infinityschool.com.br/"><img src={logo} alt="IN logo" /></a>
            </div>
            <nav className="right">
                <a href="">LOGIN</a>

            </nav>
        </header>
        
        

    );
}

export default MyHeader;