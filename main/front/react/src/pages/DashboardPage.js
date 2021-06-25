import DBLayout from "../components/Layout/DBLayout";
import NavigationBar from "../components/Dashboard/NavigationBar";
import Board from "../components/Dashboard/Board";
const DashboardPage = () => {
  return (
    <DBLayout>
      <NavigationBar />
      <Board />
    </DBLayout>
  );
};

export default DashboardPage;
