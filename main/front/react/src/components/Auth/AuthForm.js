import { useRef, useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../../store/auth-context";

import classes from "./AuthForm.module.css";

const AuthForm = () => {
  const history = useHistory();
  const usernameInputRef = useRef();
  const passwordInputRef = useRef();

  const authCtx = useContext(AuthContext);

  const submitHandler = (e) => {
    e.preventDefault();

    const enteredUsername = usernameInputRef.current.value;
    const enteredPassword = passwordInputRef.current.value;

    fetch("http://localhost:5000/auth", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: enteredUsername,
        password: enteredPassword,
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          return res.json().then((data) => {
            throw new Error(data ? data.description : "fuck, it's an error");
          });
        }
      })
      .then((data) => {
        authCtx.login(data.access_token);
        history.replace("/dashboard");
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div className={classes.container}>
      <div>
        <img className={classes.image} alt="" />
      </div>
      <h2>원룸만Lab 상품관리</h2>
      <br />
      <form onSubmit={submitHandler}>
        <div className={classes.control}>
          <label>ID</label>
          <input
            type="username"
            id="username"
            required
            ref={usernameInputRef}
          />
        </div>
        <div className={classes.control}>
          <label>PASSWORD</label>
          <input
            type="password"
            id="password"
            required
            ref={passwordInputRef}
          />
        </div>
        <div className={classes.actions}>
          <button>LOGIN</button>
        </div>
      </form>
    </div>
  );
};

export default AuthForm;
