import InputMask from 'react-input-mask';

import "./input.css"

function Input(props){
  
  return (
    <div className={"label-input " + props.className}>
      { (props.label || props.error) &&
        <div className={"div-label " + (props.errorAlignColumn ? "errorColumn" : "errorRow")}>
          { props.label && <label className="label" htmlFor={props.id}>{props.label}:{props.required && '*'} {props.optional && <i>Campo opcional</i>}</label> }
          { props.error && <p className="erro">{props.error}</p> }
        </div>
      }
      <InputMask id={props.id}
        autoFocus={props.autoFocus}
        name={props.id}
        className={"input " + (props.disabled && "disabled")}
        type={props.type}
        placeholder={props.placeholder}
        onChange={props.onChange}
        mask={props.mask}
        value={props.value}
        disabled={props.disabled}
        maskChar={props.maskChar}
      />
    </div>
  );
}

export default Input;
