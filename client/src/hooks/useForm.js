import { useState } from "react";

function useForm() {
  const [values, setValues] = useState({});
  const [errors, setErrors] = useState({});

  const cleanErrors = () => {
    setErrors({});
  }

  const handleChange = (event) => {
    setValues({ ...values, [event.currentTarget.name]: event.currentTarget.value })
    setErrors({ ...errors, [event.currentTarget.name]: undefined })
  };

  const handleSelectChange = (name, value) => {
    if (value && value.label) {
      setValues({ ...values, [name]: value.label })
    } else {
      setValues({ ...values, [name]: value })
    }

    setErrors({ ...errors, [name]: undefined })
  }

  const handleSelectStateChange = (value) => {
    const stringValue = String(value)
    setValues({ ...values, city: '-1', state: stringValue})
  }

  const updateValues = (value) => {
    setValues(value)
  }

  const handleSubmit = (checkValues, valuesAreCorrect) => async (event) => {
    event.preventDefault();

    const error = await checkValues();

    setErrors(error);

    if (Object.keys(error).length === 0) {
      valuesAreCorrect();
    }
  };

  const handleSetErrors = (error) => {
    setErrors({ ...errors, ...error })
  }

  const handleTankChange = (event, tank) => {
    setValues({ ...values, [tank]: { ...values[tank], [event.currentTarget.name]: event.currentTarget.value } })
    setErrors({ ...errors, [tank]: { ...errors[tank], [event.currentTarget.name]: undefined } })
  }
  
  return { values, errors, handleSetErrors, handleChange, handleSubmit, handleSelectChange, handleSelectStateChange, cleanErrors, handleTankChange, updateValues };
};

export default useForm;