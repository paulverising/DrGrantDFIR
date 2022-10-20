# DrGrantDFIR
Dr. Alan Grant was a visiting paleontologist to Jurassic Park. Since we use Velociraptor for IR we need a great paleontologist to help track IR cases...enter DrGrantDFIR.

---

## Primary Goals
The goal of this project is to create a solution for case management that fits the style of the Rapid7 IR team. We need to be able to track overall cases, Indicators of Compromise (IoC), Systems in scope, Accounts in scope, and a way to assign and track tasks to analysts. Each of these sections needs flexibility/customizations in the data selections. For example, we need the ability to enter in a system name, but designate the type of system it is (windows, linux, mac, server, workstation).

## Secondary Goals
Features beyond core functionality that would improve the user experience is the ability to enter in narratives about the case in question and to output reports using that narrative/data into a template. It would also be nice to have some graph functionality to see how certain entities link to one another. For example, a compromised user account was used on 3 systems, and those systems and 2 different pieces of malware.

## To Do
- [ ] build the base application
- [ ] build cases page
- [ ] build the systems page
- [ ] build the accounts page
- [ ] build the IoC's page
- [ ] build the tasks page