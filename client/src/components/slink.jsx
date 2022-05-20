import { Link } from "react-router-dom";


export default function SLink(props) {
    return (
      <Link to={props.to} style={{ textDecoration: 'none', color: '#fff',}}>
        {props.children}
      </Link>
    )
}

