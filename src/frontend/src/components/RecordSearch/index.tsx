import React from "react";
import { Redirect } from "react-router-dom";
import { useAppDispatch } from "../../redux/hooks";
import { stopDemo } from "../../redux/demoSlice";
import { hasOeciToken } from "../../service/cookie-service";
import setupPage from "../../service/setupPage";
import Layout from "./Layout";

export default function RecordSearch() {
  setupPage("Search Records");
  useAppDispatch()(stopDemo());

  if (!hasOeciToken()) return <Redirect to="/oeci" />;

  return <Layout />;
}
