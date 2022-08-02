import komand
from .schema import RemoveInput, RemoveOutput


class Remove(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove", description="Remove user", input=RemoveInput(), output=RemoveOutput()
        )

    def run(self, params={}):
        status = ""

        # user obj to remove
        u = self.connection.github_user
        g = self.connection.user
        remove_user = u.get_user(params.get("username"))
        if g == remove_user:
            self.logger.error("Run: Cannot remove your own username")
            raise Exception('Github: - "user" Failed')

        # remove from repo in organization
        if params.get("organization") and params.get("repository"):
            repo = u.get_organization(params.get("organization")).get_repo(params.get("repository"))
            repo.remove_from_collaborators(remove_user)
            status = f'Successfully removed {remove_user.name} from the repo {repo.full_name} in {params.get("organization")}'


        elif params.get("organization"):
            org = u.get_organization(params.get("organization"))
            org.remove_from_members(remove_user)
            status = f'Successfully removed {remove_user.name} from the Organization {params.get("organization")}'


        else:
            repo = g.get_repo(params.get("repository")).remove_from_collaborators(remove_user)
            status = f"Successfully removed {remove_user.name} from the repo {repo.full_name}"


        return {"status": status}
