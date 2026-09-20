class Codec {

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfsSerialize(root, sb);
        return sb.toString();
    }

    private void dfsSerialize(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("#,");
            return;
        }
        sb.append(node.val).append(",");
        dfsSerialize(node.left, sb);
        dfsSerialize(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        String[] values = data.split(",");
        int[] index = new int[1];
        return dfsDeserialize(values, index);
    }

    private TreeNode dfsDeserialize(String[] values, int[] index) {
        if (values[index[0]].equals("#")) {
            index[0]++;
            return null;
        }

        TreeNode node = new TreeNode(Integer.parseInt(values[index[0]++]));
        node.left = dfsDeserialize(values, index);
        node.right = dfsDeserialize(values, index);
        return node;
    }
}
