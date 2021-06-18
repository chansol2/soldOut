import { useContext } from "react";
import { Switch, Route, Redirect } from "react-router-dom";

import AuthPage from "./pages/AuthPage";
import DashboardPage from "./pages/DashboardPage";
import AuthContext from "./store/auth-context";

function App() {
  const authCtx = useContext(AuthContext);
  return (
    <Switch>
      <Route path="/auth">
        {!authCtx.isLoggedIn && <AuthPage />}
        {authCtx.isLoggedIn && <Redirect to="/dashboard" />}
      </Route>
      <Route path="/dashboard">
        {authCtx.isLoggedIn && <DashboardPage />}
        {!authCtx.isLoggedIn && <Redirect to="/auth" />}
      </Route>
    </Switch>
  );
}

export default App;
