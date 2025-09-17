import "./Button.css";

function Button(props){
    return(
        <div>
            <button className="Button">{props.name}</button>
        </div>
        
    );
}

export default Button;