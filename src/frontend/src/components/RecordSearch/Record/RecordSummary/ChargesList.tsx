import React from "react";
import { getEligibilityColor } from "./utils";

interface ChargeProps {
  id: string;
  name: string;
  hasBalance: boolean;
}

interface ChargesProps {
  caseWithBalanceHeader: string;
  charges: any[];
}

interface EligibilityGroupProps {
  eligibility: string;
  headerAndCharges: any[];
}

interface ChargeListProps {
  chargesGroupedByEligibilityAndCase: { [label: string]: any[] };
  totalCharges: number;
}

function Charge({ id, name, hasBalance }: ChargeProps) {
  return (
    <li className="f6 bb b--light-gray pv2">
      <a href={"#" + id} className={hasBalance ? "ml2" : "link hover-blue"}>
        {name}
      </a>
    </li>
  );
}

function Charges({ caseWithBalanceHeader, charges }: ChargesProps) {
  return (
    <>
      {caseWithBalanceHeader && (
        <li key={caseWithBalanceHeader} className="fw7 pt2">
          {caseWithBalanceHeader}
        </li>
      )}
      {charges.map(([id, name]: [string, string]) => {
        return (
          <Charge
            key={id}
            id={id}
            name={name}
            hasBalance={caseWithBalanceHeader !== ""}
          />
        );
      })}
    </>
  );
}

function EligibilityGroup({
  eligibility,
  headerAndCharges,
}: EligibilityGroupProps) {
  const labelColor = getEligibilityColor(eligibility);
  const numCharges = headerAndCharges.reduce(
    (acc: number, aCase: any) => acc + aCase[1].length,
    0
  );

  return (
    <div className="mb3">
      <div className={labelColor + " bb b--light-gray lh-copy pb1"}>
        <span className="fw7 mb2">{eligibility}</span>{" "}
        {numCharges > 0 && `(${numCharges})`}
        {eligibility === "Needs More Analysis" && (
          <p className="f6 fw5">
            These charges need clarification below before an accurate analysis
            can be determined
          </p>
        )}
      </div>

      <ul className="list">
        {headerAndCharges.map(([caseWithBalanceHeader, charges], idx) => (
          <Charges
            key={idx}
            caseWithBalanceHeader={caseWithBalanceHeader}
            charges={charges}
          />
        ))}
      </ul>
    </div>
  );
}

export default function ChargesList({
  chargesGroupedByEligibilityAndCase,
  totalCharges,
}: ChargeListProps) {
  return (
    <>
      <h3 className="bt b--light-gray pt2 mb3">
        <span className="fw7">Charges</span> ({totalCharges})
        <p className="f6 fw5 pt1">Excludes traffic violations</p>
      </h3>

      {Object.entries(chargesGroupedByEligibilityAndCase).map(
        ([eligibility, headerAndCharges]) => {
          return (
            <EligibilityGroup
              key={eligibility}
              eligibility={eligibility}
              headerAndCharges={headerAndCharges}
            />
          );
        }
      )}
    </>
  );
}
