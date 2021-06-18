import { useContext } from "react";
import { useHistory } from "react-router-dom";
import AuthContext from "../store/auth-context";

const DashboardPage = () => {
  const history = useHistory();
  const authCtx = useContext(AuthContext);
  const logoutHandler = (e) => {
    e.preventDefault();
    console.log(authCtx.isLoggedIn);
    authCtx.logout();
    console.log(authCtx.isLoggedIn);

    history.replace("/auth");
  };

  return (
    <div>
      <h1>Dashboard Page</h1>
      <button onClick={logoutHandler}>Log out</button>
    </div>
  );
};

export default DashboardPage;
