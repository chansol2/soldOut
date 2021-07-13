import { Route, Switch } from "react-router-dom";

import MainLayout from "../components/Layout/MainLayout";
import Dashboard from "../components/Dashboard/Dashboard";
import Update from "../components/Update/Update";
import Upload from "../components/Upload/Upload";
import Delete from "../components/Delete/Delete";
import RCMD from "../components/RCMD/RCMD"


const MainPage = () => {
  return (
    <MainLayout>
      <Switch>
        <Route path="/dashboard">
          <Dashboard />
        </Route>
        <Route path="/update">
          <Update />
        </Route>
        <Route path="/upload">
          <Upload />
        </Route>
        <Route path="/delete">
          <Delete />
        </Route>
        <Route path="/rcmd">
          <RCMD />
        </Route>
      </Switch>
    </MainLayout>
  );
};

export default MainPage;
