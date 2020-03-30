# Benefits and The Revision Process

## Revision Process

Any changes to this document must be applied through GitHub pull requests.
Each pull request must be approved by Sam and the president of Computerization to be merged into
master.
To maintain a clean commit history, it should be merged into master by 'squash and merge'.
This policy should be strictly enforced by GitHub’s branch protection feature.
Commits in the pull request must be signed (having a green Verified badge in commit page) and its
author must have GitHub 2-factor authentication enabled to have legal effect.

Once this agreement is finalized, Sam does not have the right to unilaterally end the sponsorship,
unless under extreme circumstances. However, Computerization has the right to end this sponsorship
at any time and Sam has the ultimate right to interpret this document in any reasonable way.

This agreement must be manually renewed each year, while Sam is not at work.

## Benefits List

Note:

- All benefits in this section should be considered independently.
- The funds are not available during Sam’s internship. As mitigation, more funds will be provided
  prior to Sam’s internship.

### General Responsibilities

All the funds specified in sections below can only be used for activities that are directly related
to Computerization. It is strictly prohibited to use them for personal purposes or other clubs.

Sam must be informed about how these funds are being used monthly. This requirement can be fulfilled
by inviting Sam to a group chat about fund allocation or making the information available on
Computerization website.

To avoid abuse of the fund of club leaders, every member should be informed about the existence of
this sponsorship, and members have the right to question the usage of the fund and ways to
anonymously report to Sam about concerns without concerns of retaliation.

There will likely be unused budgets at the end of the academic year. The remaining money must be
securely transferred to the next Computerization leader.

### Prioritized Referrals

Sam will try to offer tech company referral opportunities to all Computerization members with high
priority. However, members are not guaranteed this opportunity. Sam will try to assess resumes of
members to give feedback. However, feedback is not guaranteed to help you improve your chances of
entering any tech company since Sam is not an expert on this matter.

Unlike other benefits, this benefit is always active and will remain active in the foreseeable
future.

### Technical Consulting

Feel free to ask Sam about technical decisions while he is not doing his internship. The questions
may include architecture, static typing, technical stack, development best practices, etc. However,
Sam will not answer questions about club management issues, like how to deal with the school’s
administrator, unmotivated members, low morale, etc.

### Personal Website Cost Reimbursement

All members of Computerization, past or present, will receive full reimbursement of their personal
websites cost until the end of their college freshmen year, given that the following requirements
are satisfied:

1. The personal website must be open sourced on GitHub with one of the licenses listed on the
   [Choose A License website](https://choosealicense.com/appendix/).
2. The personal website must be relatively complete. For example, a website that only contains
   'Hello world!' is not considered as complete.
3. The personal website backend must not run crazily expensive computations
   (e.g. mining cryptocurrencies).
4. The personal website must be deployed on machines with reasonable hardware capacity. For
   example, a single-page static website deployed to 96-core CPU, 1TB memory and 256TB SSD will not
   be considered as reasonable.

### Development/Deployment Cost Reimbursement

All allowed items in [`APPROVED_REIMBURSEMENT_LIST.md`](./APPROVED_REIMBURSEMENT_LIST.md) will be
fully reimbursed. However, Computerization members must make some faithful attempt to minimize the
cost.

### Encouragement Funds

These encouragement funds will be directly given as reimbursements to 3 top contributors to
Computerization projects, with ratio 4:3:3. Receivers can only spend these funds on personal
CS-related development, such as building personal websites, doing machine learning experiment, or
playing with Kubernetes clusters in the cloud.

#### Better Infrastructure Encouragement Fund

Computerization will receive $100 amount of fund for all completed items below. If they are partially
enforced, then Computerization will receive $40.

- Linter/auto formatter has been correctly set up to enforce code style.
- Members have their GitHub account two-factor authenticated.
- Each commit is GPG signed.
- Continuous integration that tests non-trivial properties of programs.
- Continuous deployment that deploys every merged pull request (master branch) to the staging
  environment.

#### Better Engineering Encouragement Fund

If Computerization can enforce the following list of practices over 90% of the time, then
Computerization will receive $100. If they are enforced over half of the time, then Computerization
will receive $40.

- GitHub branch protection: No one can commit to the master branch without at least one pull request
  approval.
- No pull requests that fail CI tests can be merged. Having zero or only trivial CI tests do not
  count as completion of this item.
- Computerization can maintain its official website and have a blog that proudly documents its
  engineering practices.
- README and CHANGELOG of Computerization repositories have been constantly maintained.

#### Cleaner Codebase Encouragement Fund

Computerization will receive $100 for each completed item below:

- Have over 70% of type coverage for one part of the codebase.

### Random Activity Funds

Computerization will get up to $100 to hold whatever the team event they like. A team event is
defined as an event that only and at least three Computerization members attend.
