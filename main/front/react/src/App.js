import { useContext } from "react";
import { Switch, Route, Redirect } from "react-router-dom";

import AuthPage from "./pages/AuthPage";
import MainPage from "./pages/MainPage";
import AuthContext from "./store/auth-context";

function App() {
  const authCtx = useContext(AuthContext);
  return (
    <Switch>
      <Route  path="/" exact>
        {authCtx.isLoggedIn && <Redirect exac to="/dashboard" />}
        {!authCtx.isLoggedIn && <Redirect to="/auth" exact/>}
      </Route>
      <Route path="/auth" exact >
        {!authCtx.isLoggedIn && <AuthPage />}
        {authCtx.isLoggedIn && <Redirect to="/dashboard" />}
      </Route>
      <Route  exact path={[
        "/dashboard",
        "/update",
        "/upload",
        "/delete",
        "/rcmd"
      ]} >
        {authCtx.isLoggedIn && <MainPage />}
        {!authCtx.isLoggedIn && <Redirect to="/auth" exact/>}
      </Route>
    </Switch>
  )
}

export default App;
